from Hate_Speech_Detection.logger import logging
from Hate_Speech_Detection.exception import CustomException
import sys

try:
    a = 7/"0"


except Exception as e:
    raise CustomException(e, sys) from e



# logging.info("welcome to our project again re-run")            #everytime i run the folder , it will create a log