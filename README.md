# upload-log-collector-azure-table-storage

In order to connect python application to Azure storage account.

1. You need to create Azure storage account on your Azure subscription 
2. You need to install python dependencies given in requiements.txt
3. You need to create table name example:devices on your Azure storage account
4. You need to configure only two parameters to connect client to storage account
   - Azure storage account name
   - Shared Access Key (create SAS on Azure account under security + networking) 
5. Run python3 main.py
6. On successfull execution the content of both TAIHB1166038_TvInfo uploaded on Azure table storage account 
