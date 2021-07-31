# moxaiiot-upload-device-info-azure-table-storage

In order to connect python application to Azure storage account.

1. You need to create Azure Storage Account on your Azure subscription. 
2. You need to install python dependencies given in requiements file
3. You need to create table (devices) on your Azure storage account
4. You need to configure only two parameters to connect client to storage account
   - Azure storage account name
   - Shared Access Key (create SAS on Azure account under security + networking) 
5. Run python3 main.py
6. On successfull execution the content of both TAILB1015980_deviceInfo and TAILB1015981_deviceInfo files uploaded on Azure storage account 
   where PartitionKey is same for all entries given in the config file "moxa:sphinx"
   and RowKey is the Serial Number of the device 
