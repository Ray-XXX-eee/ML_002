import os
import sys
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO,format = '%(asctime)s - %(name)s - %(message)s')

project_name = 'ml_002-wine_pred'

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/config.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "parse.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)
    
    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created directory: {file_dir} for the file {file_name}")
        
    if (not os.path.exists(file_path) or os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as file:
            logging.info(f"Created file: {file_name}")
    else:
        logging.info(f"File already exists: {file_name}")
        
logging.info("Project structure created successfully!")