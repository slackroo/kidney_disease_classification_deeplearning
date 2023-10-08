import os
from pathlib import Path
import logging

# logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'CNNClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "images/image_scripts/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    # for flask, we will create a template with .html
    "templates/index.html",
]

for file_path in list_of_files:
    if file_path.endswith("/"):  # Check if it's a directory path
        directory_path = file_path
        os.makedirs(directory_path, exist_ok=True)
        logging.info(f"Creating directory: {directory_path}")
    else:
        file_path = Path(file_path)
        file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory; {file_dir} for file: {file_name}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            logging.info(f"creating empty file: {file_path}")

    else:
        logging.info(f"{file_name}  is already existing ")






