import os

# list of files you want to create
list_of_files = [
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    "notebooks/.gitkeep",
    "src/cnnClassifier/__init__.py",
    "src/cnnClassifier/utils/__init__.py",
    "src/cnnClassifier/utils/logger.py",
    "src/cnnClassifier/utils/common.py",
    "src/cnnClassifier/components/__init__.py",
    "src/cnnClassifier/config/__init__.py",
    "src/cnnClassifier/pipeline/__init__.py",
    "src/cnnClassifier/entity/__init__.py",
    "src/cnnClassifier/constants/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "setup.py",
    "main.py",
    "README.md",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass

