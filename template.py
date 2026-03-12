import os
from pathlib import Path


list_of_files = [
    ".github/workflows/ci.yaml",
    ".github/workflows/python-publish.yaml",
    "src/mongodbconnector/__init__.py",

    # Source files
    "src/mongodbconnector/components/__init__.py",
    "src/mongodbconnector/components/data_ingestion.py",
    "src/mongodbconnector/components/data_transformation.py",
    "src/mongodbconnector/components/model_trainer.py",
    "src/mongodbconnector/components/model_evaluation.py",

    "src/mongodbconnector/pipeline/__init__.py",
    "src/mongodbconnector/pipeline/training_pipeline.py",
    "src/mongodbconnector/pipeline/prediction_pipeline.py",

    "src/mongodbconnector/utils/__init__.py",
    "src/mongodbconnector/utils/utils.py",

    "src/mongodbconnector/logger/__init__.py",
    "src/mongodbconnector/logger/logging.py",
    
    "src/mongodbconnector/exception/__init__.py",
    "src/mongodbconnector/exception/exception.py",
    
    # MongoDB layer
    "src/mongodbconnector/database/__init__.py",
    "src/mongodbconnector/database/mongodb_connection.py",
    "src/mongodbconnector/database/mongodb_crud.py",

    # Tests
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",

    # Project files
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",

    # Experiment notebook
    "experiment/experiments.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        #logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        print(f"Created: {filepath}")
        #logging.info(f"Creating empty file: {filepath}")
