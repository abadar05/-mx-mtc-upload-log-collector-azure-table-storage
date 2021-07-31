#!/usr/bin/env python 3

import logging
import datetime
from lib.config_module import Config_BaseClass
from azure.cosmosdb.table.tableservice import TableService
from azure.common import AzureConflictHttpError


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


class Device_InfoClass(Config_BaseClass):

    def __init__(self, **kwargs):
        
        Config_BaseClass.__init__(self, **kwargs)
        # Access Init() propties of Config Base Class
        try:
            self._table = TableService(account_name= self._account_name, sas_token= self._sas_token)
        except ValueError:
            logger.error("MISSING Info. You need to provide an account name or sas_token when creating a storage service.")
        self._device = {'PartitionKey': self._partition_key}

    def create_table(self, readlines):
        # Note: self._device['dev_sn'] is VALID but self._device['dev sn'] is INVALID 
        # space are not allowed in the property  
        for line in readlines:
            if "SN" in line:         
                key = line.split(":")[0]
                sn = line.split(":")[1]   
                sn = sn.rstrip("\n")
                sn = sn.replace('"','')    
                self._device['RowKey'] = sn
                self._device['dev_sn'] = sn
            if "Deamon" in line:
                key = line.split(":")[0]
                deamon = line.split(":")[1]
                deamon = deamon.rstrip("\n")
                deamon = deamon.replace('"','')    
                self._device['TeamViewer_deamon'] = deamon
            if "Status" in line:
                key = line.split(":")[0]
                status = line.split(":")[1]
                status = status.rstrip("\n")
                status = status.replace('"','')    
                self._device['Agent_status'] = status
            if "Cloud Connectivity" in line:
                key = line.split(":")[0]
                conn = line.split(":")[1]
                conn = conn.rstrip("\n")
                conn = conn.replace('"','')    
                self._device['Cloud_Connectivity'] = conn
        # Date of Production 
        self._device['ord_ts'] = datetime.datetime.utcnow().isoformat()+'Z'
        # Order reference number
        self._device['ord_ref'] = self._order_id
        logger.info("TABLE: {}".format(self._device))
        return self._device
        
    def publish_table(self, device):
        """
        Inserts a new entity into the table. Throws if an entity with the same 
        PartitionKey and RowKey already exists.
        """
        try:
            # Add entity (device info) into Azure Storage Table name devices 
            self._table.insert_entity('devices', device)
            return True
        except AzureConflictHttpError as e:
            #print(e) 
            return False
        


