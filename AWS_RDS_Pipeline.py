import pandas as pd
import csv
import os
import numpy as np
import psycopg2
from PostgreSql_access import password
from PostgreSql_access import host

'''
- Import the CSV file into pandas
- Clean the table name and remove all extra symbols, spaces, capital letters
- The goal is to complete tasks that are too complex for a database
- Clean the column header and remove all extra symbols, spaces, capital letters
- Import the data into AWS PostgreSQL'''


df = pd.read_csv('/Users/vbfitnest/Downloads/CSV_Automation/Customer Contracts$.csv')

#clean table names
# - lower case letters
# - remove white space
# - remove -,/,\\, $

file = "Customer Contracts$"

#Apply various data cleansing patterns to file name
clean_tbl_name = file.lower().replace(" ","_").replace("#","") \
.replace("-","_").replace(r"/","_").replace("\\","_").replace("?","") \
.replace(")","").replace(r"(","").replace("$","")

#List comprehension that loops through list of column names and remove unwanted characters
df.columns = [x.lower().replace(" ","_").replace("","") \
.replace("-","_").replace(r"/","_").replace("\\","_").replace("*","") \
.replace(")","").replace(r"(","").replace("$","").replace("#","") for x in df.columns]

#Sql statement that will create our table.
sql_table = '''create table customer contracts (
    customer_name       varchar,
    start_date          varchar,
    end_date            varchar,
    contract_amount_m   float,
    invoice_sent        varchar,
    paid                varchar,
    );'''

#When we import a file into a pandas dataframe, this file is assigned pandas data types.
#We need to change the pandas data types to match the database in which we will be sending this data(PostgreSql)

replacements ={'object' : 'varchar' ,'float64' : 'float',
              'int64' : 'int', 'datetime64' : 'timestamp',
              'timedelta64[ns]' : 'varchar'}



#This code replaces the pandas data types with the postgreSql data types, join them with the Sql column names,
#place a comma after the name and data type and repeat this process for each column.
col_str = ",".join("{} {}".format(n, d) for (n, d) in zip(df.columns, df.dtypes.replace(replacements)))

#Create the postgreSQL database connection with the psycopg2 api.
#You will use the host information to connect to your RDS instance; therefore keep this information handy.
#Another rule of thumb is to never put password directly onto a file due to sql injection concerns.
#I saved my host and password as string variables on a local file and imported them both for this project.

conn = psycopg2.connect(host= host,
                        dbname='my_database',
                        user='postgres',
                        password = password)

cursor = conn.cursor()
print('Opened database successfully')

# Create table
cursor.execute("Drop table if exists customer_contracts;")

cursor.execute("create table customer_contracts (customer_name varchar, start_date varchar, end_date varchar,\
               contract_amount_m float, invoice_sent varchar, paid varchar)")

#Changing the working directory to send the csv to another folder
os.chdir('/Users/vbfitnest/PycharmProjects/pythonProjects/venv/datasets/Output')

#Save the new formatted dataframe into a CSV file
df.to_csv('customer_contracts.csv', header=df.columns, index=False, encoding='utf-8')
#
# Open CSV file in memory
my_file = open('customer_contracts.csv')
print('file opened in memory')

# Copy contents of the CSV file into PostgreSQL RDS instance
Sql_query = '''
COPY customer_contracts FROM STDIN With
    CSV
    Header
    Delimiter As',' 
'''

try:
    cursor.copy_expert(Sql_query, file = my_file)
except:
    print('Something Went Wrong')

#Make database accessible by multiple users

cursor.execute ("grant select on table customer_contracts to public")

#Always commit for changes to take effect and close the connect afterwards
conn.commit()

cursor.close()

print("Table customer_contracts import to db completed")

