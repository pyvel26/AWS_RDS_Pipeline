### AWS_RDS_Pipeline
# CREATE YOUR FIRST CLOUD DATA PIPELINE :computer::cloud:

## Description

All Data professionals should know how to navigate the cloud and effective use these services to best service the client. The purpose of this project was to start gaining experience working with data in the cloud. This project is a simple Data Cleansing ETL Pipeline using **SQL, Python, AWS RDS(PostgreSQL)and AWS Free Tier Account.**

## Before You Get Started

Select a CSV file to use for this project. I recommend a file without many rows of data as it’s easier to work with for practice.  Your data should be messy because we are going to clean the column names and rows with the pandas library in Python. If you're data isn't messy, then add characters to your column names and throughout the data as I did in the BEFORE screenshot on my project documents page.

## AWS Free Tier Account

With your Free AWS account, you can create an AWS RDS instance for PostgreSQL; however, you will need to choose version 12 or earlier since they are the only versions on the free tier. After you've set up your AWS free tier account and the AWS RDS PostgreSQL instance, look at the AWS_RDS_Pipeline.py file for step-by-step instructions on my data cleansing process. 

Open your favorite interpreter and import all the necessary libraries. Feel free to make this project your own.

## Libraries:

- import pandas as pd
- import csv
- import os
- import psycopg2


At this point, you've created the AWS free tier account, AWS RDS instance for PostgreSQL and successfully ran your python script.
In order to view your database and the table created by this script, you will need to access your PostgreSQL instance by any GUI for PostgreSQL. I posted the screenshots for PgAdmin and the instructions below to accomplish this task.

## :boom::boom:Connecting PgAdmin to AWS RDS PostgreSQL instance:boom:
- Log into Pgadmin
- Right click servers and select Create
- On the General Tab,enter your AWS RDS server name
- Click on the Connection tab and copy your RDS host name, maintenance name (database name) and username. 
- Select Save and now you should be able to navigate to the database and table you created from this project.



## :skull_and_crossbones:Handling Passwords In Scripts
Never put raw passwords or access codes in your scripts. For this project, I chose to create a python script and save my password and host as a string variable.
Next, I imported both variables (host, password) in the data cleansing script as shown below.  When you create the database connection, you can simply put the word 'host' and 'password' instead of type the actual information.  The script will read the actual string from the python script you've imported.  



from PostgreSql_access import password\
from PostgreSql_access import host


## Link To My Data Analysis Portfolio
(https://www.behance.net/gallery/127131435/Data-Analysis-Portfolio)

Job Opportunities : :mailbox_with_mail: estervellebennett@gmail.com


:EMOJICODE:
