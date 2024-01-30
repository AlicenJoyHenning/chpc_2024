# -*- coding: utf-8 -*-
"""
PYTHON  
Extract, Transform, and Load 
"""
""" REVIEW """

import pandas as pd 
country_data = pd.read_csv("day_02\\data_02\\country_data_index.csv")

# Read in df with no header info
column_names =  ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
iris = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= column_names)

# Read in text files with semi colon separator 
geospatial_Data = pd.read_csv("data_02/Geospatial Data.txt",sep=";")

# Read in excel spreadsheet 
resident_doctors = pd.read_excel("data_02/residentdoctors.xlsx")

"""TRANSFORM """
# Parameters of the readcsv function 
# https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-read-csv-table

# Index column 
country_data = pd.read_csv("day_02\\data_02\\country_data_index.csv", index_col=0)

# Skip rows
insurance = pd.read_csv("day_01/insurance_data.csv", skiprows = 5)

# Column headings 
column_names = ["duration", "pulse", "max_pulse", "calories"]
patient_data = pd.read_csv("day_02\\data_02\\patient_data.csv",header = None,names = column_names)

# Unique delimiter 
df = pd.read_csv("day_02\\data_02\\Geospatial Data.txt", sep=";")

""" Inconsistent data types & names 

.extract() and .astype() methods that can be applies to a pandas series object 

df = pd.read_excel("day_02\\data_02\\residentdoctors.xlsx")
## 1 Extract the lower end of the age range 
df['LOWER_AGE'] = df['AGEDIST'].str.extract('(\d+)-')
## 2 Convert the new column to float 
df['LOWER_AGE'] = df['LOWER_AGE'].astype(int)

"""





