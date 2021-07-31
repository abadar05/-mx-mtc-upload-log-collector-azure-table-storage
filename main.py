#!/usr/bin/env python 3

import os 
import sys
import json
import logging
import datetime
from lib.util_module import File_IO 
from lib.device_module import Device_InfoClass

__author__ = "Amjad B."
__license__ = "MIT"
__version__ = '1.1.1'
__status__ = "beta"

log_format = '%(asctime)s: %(levelname)s - %(name)s - %(message)s'
logging.basicConfig(level=logging.INFO, datefmt="[%Y-%m-%d %H:%M:%S]", format=log_format)
logger = logging.getLogger(__name__)

# Save full log
fh = logging.FileHandler('main.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
logger.addHandler(fh)

# Save error log
fh = logging.FileHandler('main.error.log')
fh.setLevel(logging.ERROR)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
logger.addHandler(fh)

configFile = "config.json"
def read_ext_config(pathToFile):
    """
    Configuration
    """
    try:
        with open(pathToFile) as json_data_file:
            cfg_obj = json.load(json_data_file)
            logger.debug("Read External Config: {}".format(cfg_obj)) 
            return cfg_obj
    except IOError as e:
        logger.error(e)

def close_terminal(): 
   input('\n Press Enter to close the terminal window:')
   sys.exit()

def main():
    obj_ext_configuration = read_ext_config(configFile)
    obj_fileIO = File_IO(conf = obj_ext_configuration)
    obj_devInfo = Device_InfoClass(conf = obj_ext_configuration)
    logFileList = obj_fileIO.get_log_files()
    logger.info(logFileList)
    for logFile in logFileList:
        readlines = obj_fileIO.read_log_file(logFile)
        device = obj_devInfo.create_table(readlines)
        ret = obj_devInfo.publish_table(device)
        if ret == True:
            logger.info("***************************************************")
            logger.info("Table uploaded Successfully to Azure Table Storage!")
            logger.info("Result:PASSED! DeviceSN:{}".format(device['dev_sn']))
            logger.info("***************************************************")
        else:
            logger.error("*****************************************************************************") 
            logger.error("Result: FAILED! Entity Already Exists - DeviceSN:{} ".format(device['dev_sn']))
            logger.error("*****************************************************************************") 
    close_terminal()
    
if __name__ == '__main__':
    main()
