import importlib
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install(library, import_name=None, git_install=False):
    if import_name is None:
        import_name = library
    try:
        importlib.import_module(import_name)
        print(f"{library} is already installed")
    except ImportError:
        print(f"Installing {library}...")
        if git_install:
            # Special installation for tvDatafeed
            print("Checking for git...")
            try:
                subprocess.run(["git", "--version"], check=True, capture_output=True)
                print("Git is installed, proceeding with tvDatafeed installation...")
                install_cmd = f"pip install --upgrade --no-cache-dir git+https://github.com/rongardF/tvdatafeed.git"
                subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "--no-cache-dir", 
                                     "git+https://github.com/rongardF/tvdatafeed.git"])
            except subprocess.CalledProcessError:
                print("Error: Git is not installed. Please install Git first before installing tvDatafeed.")
                print("You can download Git from https://git-scm.com/downloads")
                return
        else:
            install(library)
        print(f"{library} installed successfully")

# List of libraries to install with their import names (if different)
libraries = [
    ("pandas", None),
    ("numpy", None),
    ("glob", None),  # Part of standard library in Python 3
    ("os", None),    # Part of standard library
    ("statsmodels", None),
    ("tqdm", None),
    ("tvDatafeed", "tvDatafeed", True),  # Requires special git installation
    ("pykalman", None),
    ("joblib", None),
    ("TA-Lib", "talib"),  # Note: The package name is TA-Lib but imported as talib
    ("warnings", None),   # Part of standard library
    ("matplotlib", None),
    ("seaborn", None),
    ("scikit-learn", "sklearn"),
    ("imbalanced-learn", "imblearn"),
    ("quantstats", None)
]

print("Checking and installing required libraries...")
for lib in libraries:
    if len(lib) == 3 and lib[2]:  # Special case for tvDatafeed
        check_and_install(lib[0], lib[1], git_install=True)
    else:
        if lib[0] in ['glob', 'os', 'warnings']:  # Skip standard library modules
            continue
        check_and_install(lib[0], lib[1] if len(lib) > 1 else None)

print("\nAll required libraries are installed!")