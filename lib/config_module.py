#!/usr/bin/env python 3

import logging

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


class Config_BaseClass():

    def __init__(self, **kwargs):
        
        self._ext_conf = kwargs.get('conf', None)
        logger.debug("Read External Config: {}".format(self._ext_conf))    
        
        self._account_name = None
        self._partition_key = None
        self._sas_token = None
        
        self._local_dir = None
        self._read_files = None
        self._read_all = False
        self._logfile_lastname = None
        
        self._order_id = None
        #self._testing_mode = False
        
        self.parse_configuration()
    
    # Parse config.json file        
    def parse_configuration(self):
       
        logger.info("*********** Parse Configuration ***********")
        
        if not self._ext_conf:
            logger.error('Empty configuration!')
            return False          
        
        # continue here 
        if self._ext_conf["general"]["account_name"]: 
            self._account_name = self._ext_conf["general"]["account_name"] 
            logger.info("account_name: {}".format(self._account_name))
        
        if self._ext_conf["general"]["partition_key"]: 
            self._partition_key = self._ext_conf["general"]["partition_key"] 
            logger.info("partition_key: {}".format(self._partition_key))
        
        if self._ext_conf["general"]["sas_token"]: 
            self._sas_token = self._ext_conf["general"]["sas_token"] 
            logger.info("sas_token: {}".format(self._sas_token))
        
        if self._ext_conf["directory"]["local_dir"]: 
            self._local_dir = self._ext_conf["directory"]["local_dir"] 
            logger.info("local_dir: {}".format(self._local_dir))
        
        if self._ext_conf["directory"]["read_files"]: 
            self._read_files = self._ext_conf["directory"]["read_files"] 
            logger.info("read_files: {}".format(self._read_files))
        
        if self._ext_conf["directory"]["read_all"]: 
            self._read_all = self._ext_conf["directory"]["read_all"] 
            logger.info("read_all: {}".format(self._read_all))
        
        if self._ext_conf["directory"]["logfile_lastname"]: 
            self._logfile_lastname = self._ext_conf["directory"]["logfile_lastname"] 
            logger.info("logfile_lastname: {}".format(self._logfile_lastname))
        
        if self._ext_conf["table"]["order_id"]: 
            self._order_id = self._ext_conf["table"]["order_id"] 
            logger.info("order_id: {}".format(self._order_id))
            
        logger.info("Parse Configuration Successfull! ")
        return True 
        
        
        
