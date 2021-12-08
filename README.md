# AWS_RDS_Pipeline


Description

In this project, I will show a simple ETL data pipeline using SQL, Python, AWS RDS(PostgreSQL)

Before You Get Started

Select a CSV file to use for this project. I recommend a file without many rows of data as it’s easier to work with for practice.  Your data should be messy because we are going to clean the column names and rows with the pandas library in Python. 

With your Free amazon account, you can create an AWS RDS instance for PostgreSQL; however, you will need to choose version 12 or earlier since they are the only versions on the free tier. 

Open your favorite interpreter and import all the necessary libraries. Feel free to make this project your own.

Modules:

import pandas as pd
import csv
import os
import psycopg2


After you have setup your AWS free tier account and the AWS RDS PostgreSQL instance, look at the AWS_RDS_Pipeline.py file for step-by-step instructions on my data cleansing process.
