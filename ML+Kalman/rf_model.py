import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.impute import SimpleImputer
from imblearn.over_sampling import SMOTE
import warnings
import joblib

# Suppress warnings for a cleaner output
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

def prepare_vix_data(filepath='vix_data.csv'):
    """
    Loads and preprocesses the VIX data.
    """
    print("Preparing VIX data...")
    try:
        vix_df = pd.read_csv(filepath)
        vix_df['datetime'] = pd.to_datetime(vix_df['datetime'], errors='coerce')
        vix_df = vix_df.dropna(subset=['datetime'])
        vix_df = vix_df.set_index('datetime').sort_index()
        vix_df = vix_df[['close']].rename(columns={'close': 'vix'})
        
        vix_mean_60d = vix_df['vix'].rolling(window=60).mean()
        vix_std_60d = vix_df['vix'].rolling(window=60).std()
        vix_df['vix_zscore'] = (vix_df['vix'] - vix_mean_60d) / vix_std_60d
        
        print("VIX data prepared successfully.")
        return vix_df

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found. VIX features will not be added.")
        return None

def train_profitability_model(trades_filepath='detailed_trades_features.csv', vix_data=None):
    """
    Loads trade data, analyzes feature correlation, trains a Random Forest model,
    and evaluates its performance.
    """
    print("\n--- Starting Model Training Pipeline ---")
    try:
        # 1. Load and Prepare Data
        print(f"Loading trade data from '{trades_filepath}'...")
        trades_df = pd.read_csv(trades_filepath)
        trades_df['entry_date'] = pd.to_datetime(trades_df['entry_date'])
        trades_df['profit_flag'] = (trades_df['pnlcomm'] > 0).astype(int)

        if vix_data is not None:
            print("Merging VIX data with trades...")
            vix_data.index = vix_data.index.normalize()
            trades_df = pd.merge(trades_df, vix_data, left_on='entry_date', right_index=True, how='left')
        else:
            trades_df['vix'] = np.nan
            trades_df['vix_zscore'] = np.nan
        
        trades_df['is_high_vix'] = (trades_df['vix_zscore'] > 1).astype(int)
        trades_df['is_low_vix'] = (trades_df['vix_zscore'] < -1).astype(int)
        trades_df['z_score_slope'] = trades_df['z_score'].diff(3)
        trades_df['z_score_abs'] = np.abs(trades_df['z_score'])


        # 2. Define Features and Split Data by Date
        features = [
             'spread_volatility', 'hedge_ratio', 'spread_ma_ratio', 
            'spread_momentum', 'rsi1', 'atr1_norm', 
            'macd1', 'rsi2', 'atr2_norm', 
             'is_high_vix', 'is_low_vix', 'z_score_slope',
            'z_score_abs'
        ]
        target = 'profit_flag'

        for col in features:
            if col not in trades_df.columns:
                trades_df[col] = np.nan

        print("Splitting data into training and testing sets...")
        train_df = trades_df[trades_df['entry_date'] <= '2022-12-31']
        test_df = trades_df[(trades_df['entry_date'] > '2022-12-31') & (trades_df['entry_date'] <= '2024-07-31')]

        X_train = train_df[features]
        y_train = train_df[target]
        X_test = test_df[features]
        y_test = test_df[target]

        # 3. Handle Missing Values with Imputation
        print("Handling missing values using Median Imputation...")
        imputer = SimpleImputer(strategy='median')
        X_train_imputed = pd.DataFrame(imputer.fit_transform(X_train), columns=features, index=X_train.index)
        X_test_imputed = pd.DataFrame(imputer.transform(X_test), columns=features, index=X_test.index)
        
        # --- 4. NEW: CORRELATION ANALYSIS ---
        print("\n--- Feature Correlation Analysis ---")
        corr_matrix = X_train_imputed.corr()

        # Plotting the heatmap
        plt.figure(figsize=(16, 12))
        sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', linewidths=.5)
        plt.title('Feature Correlation Matrix')
        plt.show()

        # Finding and printing highly correlated pairs
        print("\nHighly Correlated Feature Pairs (absolute value > 0.7):")
        # Create a boolean mask for the upper triangle
        upper_tri = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
        # Find index pairs of features with correlation greater than 0.7
        highly_correlated_pairs = [column for column in upper_tri.columns if any(upper_tri[column].abs() > 0.7)]
        
        found_pair = False
        for col in highly_correlated_pairs:
            correlated_with = upper_tri[col][upper_tri[col].abs() > 0.7].index.tolist()
            for row in correlated_with:
                print(f"- {row} and {col}: {corr_matrix.loc[row, col]:.4f}")
                found_pair = True
        
        if not found_pair:
            print("No feature pairs with correlation > 0.7 found.")
        
        # --- END OF CORRELATION ANALYSIS ---

        # 5. Apply SMOTE to the Imputed Training Data
        print("\nApplying SMOTE to balance the training data...")
        smote = SMOTE(random_state=42)
        X_train_resampled, y_train_resampled = smote.fit_resample(X_train_imputed, y_train)

        # 6. Train the Random Forest Model
        print("\nTraining Random Forest model on imputed and balanced data...")
        rf_model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
        rf_model.fit(X_train_resampled, y_train_resampled)
        print("Model training complete.")

        # 7. Evaluate the Model
        print("\n--- Model Evaluation (Random Forest) ---")
        y_pred = rf_model.predict(X_test_imputed)

        print("\nClassification Report (after Imputation and SMOTE):")
        print(classification_report(y_test, y_pred, target_names=['Loss', 'Profit']))

        cm = confusion_matrix(y_test, y_pred)
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                    xticklabels=['Predicted Loss', 'Predicted Profit'], 
                    yticklabels=['Actual Loss', 'Actual Profit'])
        plt.title('Confusion Matrix (Random Forest)')
        plt.ylabel('Actual')
        plt.xlabel('Predicted')
        plt.show()

        # 8. Feature Importance
        importances = pd.Series(rf_model.feature_importances_, index=features)
        importances = importances.sort_values(ascending=False)
        
        plt.figure(figsize=(12, 8))
        sns.barplot(x=importances.values, y=importances.index, palette='viridis')
        plt.title('Feature Importance (Random Forest)')
        plt.xlabel('Importance Score')
        plt.ylabel('Features')
        plt.tight_layout()
        plt.show()
        
        # 6a. Save the Model and Imputer
        print("\nSaving model and imputer to disk...")
        joblib.dump(rf_model, 'rf_profitability_model.joblib')
        joblib.dump(imputer, 'feature_imputer.joblib')
        print("Model and imputer saved successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{trades_filepath}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    vix_features_df = prepare_vix_data()
    train_profitability_model(vix_data=vix_features_df)
    


