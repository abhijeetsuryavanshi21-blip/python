import sys

modules = [
    "numpy",
    "pandas",
    "scipy",
    "sklearn",
    "matplotlib",
    "seaborn",
    "xgboost",
    "lightgbm",
    "statsmodels",
    "openpyxl",
    "ipykernel",
]

print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version.split()[0]}\n")

all_good = True
for mod in modules:
    try:
        m = __import__(mod)
        version = getattr(m, "__version__", "installed")
        print(f"  [OK] {mod} (v{version})")
    except Exception as e:
        print(f"  [FAIL] {mod}: {e}")
        all_good = False

if all_good:
    print("\nAll machine learning libraries imported successfully!")
else:
    print("\nSome libraries encountered issues.")
