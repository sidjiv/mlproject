import logging  # log of execution in files , errors , custom errors
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # txt file will get created using this name
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) # os.getcwd-> current working directory, # erevy file will start with logs
os.makedirs(logs_path,exist_ok=True) #append the file

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,  
)
#PRINT specific message in info

if __name__=="__main__":
    
    try:
        a=1/0
    except:
        raise CustomException
        logging.info("Logging has started")