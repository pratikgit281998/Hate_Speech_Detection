import os                                       #Provides a way to interact with the operating system, such as creating directories and files.
from pathlib import Path
import logging                                    #to show log in the terminal while executing this file, Used to log messages to the console or a file, which helps in tracking the execution and debugging.

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

#Configures the logging module to log messages at the INFO level and above.
#The format '[%(asctime)s]: %(message)s:' includes the timestamp and the log message.

project_name = "Hate_Speech_Detection"

list_of_files = [
    f"{project_name}/components/__init__.py", # need to create a constructor file in every folder, here i am creating folder structure
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/gcloud_syncer.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/train_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/ml/__init__.py",
    f"{project_name}/ml/model.py",
    "app.py",
    "demo.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    ".dockerignore"
]


#code to create folders with script

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)
    

    if filedir !="":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating directory; {filedir} for the file : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating emoty file : {filepath}")

    else:
        logging.info(f"{filename} is already exists")