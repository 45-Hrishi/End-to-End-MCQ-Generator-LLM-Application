import logging
import os
from datetime import datetime

# Create the folder for the logs
LOG_PATH = os.path.join(os.getcwd(),"logs")
os.makedirs(LOG_PATH,exist_ok=True)

# Create the file path for files present inside logs
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_PATH,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s'
)