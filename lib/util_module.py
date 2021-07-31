#!/usr/bin/env python 3

import os 
import logging
from lib.config_module import Config_BaseClass

__author__ = "Amjad B."
__license__ = "MIT"
__version__ = '1.1.1'
__status__ = "beta"

log_format = '%(asctime)s: %(levelname)s - %(name)s - %(message)s'
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


class File_IO(Config_BaseClass):

    def __init__(self, **kwargs):
        
        Config_BaseClass.__init__(self, **kwargs)
        # Access Init() propties of Config Base Class
        
        self._fileList = []

    def read_log_file(self, pathToFile):
        """
        Configuration
        """
        try:
            with open(pathToFile) as log_file:
                readlines = (log_file.readlines())
                logger.debug("Read Device Info: {}".format(readlines)) 
                return readlines
        except IOError as e:
            logger.error(e)

    def get_log_files(self):
                          
        logger.info("Local Dir: {}".format(self._local_dir))
        logger.info("Read Files: {}".format(self._read_files))
                
        getFileList = self._read_files
        getFileDict = {key: None for key in getFileList} 
            
        directory = os.listdir(self._local_dir)
        logger.info("Return Local Files: {}".format(directory))          
        if self._read_all:
            for filename in directory:
                if not filename.startswith('.'): 
                    fname, ftype = os.path.splitext(filename)
                    if ftype == ".log":
                        lastname = fname.split("_")[-1]
                        if lastname == self._logfile_lastname:
                            fpath = os.path.join(self._local_dir + "/" + filename)
                            logger.info("LOG FILE: {}".format(fpath))
                            self._fileList.append(fpath)
            return self._fileList
        else: 
            for filename in directory:  
                if filename in getFileDict: 
                    fpath = os.path.join(self._local_dir + "/" + filename)
                    logger.info("LOG FILE: {}".format(fpath))
                    self._fileList.append(fpath)
            for key, value in getFileDict.items():
                if key not in directory:
                    logger.error("**********************************************************************************") 
                    logger.error(" {} Not Found in Local Directory {}".format(key, self._local_dir))  
                    logger.error("**********************************************************************************") 
            return self._fileList
         
