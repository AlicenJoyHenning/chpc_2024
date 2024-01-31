# -*- coding: utf-8 -*-
"""
PYTHON : Extract, Transform, and Load 
"""

""" SECTION 1 : REVIEW """
# File directories 
# (look on RHS) But making a project in spyder is different only because it is connected to Sypder 

import pandas as pd # first thing we do (we can call it whatever we want, 'pd' is shorter so its helpful)

# Load data with absolute path to the file 
country_data = pd.read_csv("C:/Users/alice/CHPC\\day_02\\data_02\\country_data_index.csv")

# Relative path : from where we are, not in full "look relative to where i am"
country_data = pd.read_csv("day_02\\data_02\\country_data_index.csv")
#### NOTE (cool): easy way click on file & you can get absolute or relative path 

# Read in df with no header info
column_names =  ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'] # list 
iris = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= column_names)
# Same as before reading from a different location online 
url = "https://raw.githubusercontent.com/kode2go/nithecs/main/lecture_01/iris.csv"
file = pd.read_csv(url, header=None, names= column_names)

# Read in text files with semi colon separator 
geospatial_data = pd.read_csv("day_02/data_02/Geospatial Data.txt",sep=";")

# Read in excel spreadsheet 
resident_doctors = pd.read_excel("day_02/data_02/residentdoctors.xlsx")

file = pd.read_json("day_02/data_02/student_data.json")
# categorical filtering would be helpful

# webscraping : beautiful soup 


url = "https://raw.githubusercontent.com/Asabele240701/css4_day02/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"
df = pd.read_csv(url)
# NOTE COOL : ctrl 1 to comment out! 

df = pd.read_csv("day_02/data_02/Accelerometer_data.csv", names = ["date_time", "x", "y", "z"])



""" SECTION 2 : TRANSFORM """

# Parameters of the readcsv function 
# https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-read-csv-table

# Index column 
country_data = pd.read_csv("day_02/data_02/country_data_index.csv", index_col=0)
# Skip rows
insurance = pd.read_csv("day_01/insurance_data.csv", skiprows = 5)
# Column headings 
column_names = ["duration", "pulse", "max_pulse", "calories"]
patient_data = pd.read_csv("day_02\\data_02\\patient_data.csv",header = None,names = column_names)
# Unique delimiter 
df = pd.read_csv("day_02\\data_02\\Geospatial Data.txt", sep=";")

""" Inconsistent data types & names """
# .extract() and .astype() methods that can be applies to a pandas series object 

df = pd.read_excel("day_02\\data_02\\residentdoctors.xlsx")
""" 
Problems : 
1. snake case vs lower case 
2. age groups '30-34yrs'
3. mixing text with numbers 

Change way info is stored into two cols, lower & upper 30-34 yrs > 30 , 34 
1 Extract the lower end of the age range 
df['LOWER_AGE'] = df['AGEDIST'].str.extract('(\d+)-')
2 Convert the new column to float 
df['LOWER_AGE'] = df['LOWER_AGE'].astype(int)

"""

df.info()
"""
RangeIndex: 161 entries, 0 to 160
Data columns (total 10 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   AGE                  161 non-null    int64  
 1   ghqscore_sum         161 non-null    float64
 2   jobsatisfaction_sum  161 non-null    float64
 3   workload_sum         161 non-null    float64
 4   AGEDIST              161 non-null    object 
 5   MARITALSTATUS        161 non-null    object # defines entire column as text because of 1 'other'
 6   CHILDREN             158 non-null    float64
 7   female               161 non-null    int64  
 8   HOURSWORKED          161 non-null    float64
 9   LOWER_AGE            161 non-null    int32  
dtypes: float64(5), int32(1), int64(2), object(2)
memory usage: 12.1+ KB
"""
# Just copies the column 
# df['LOWER_AGE'] = df["AGEDIST"]

# Extract the lowest using regular expressions
# (\d+)- first digit
df['LOWER_AGE'] = df["AGEDIST"].str.extract('(\d+)-')
# above applies the string operation (.str) AND other operations 

print(df.info())
df['LOWER_AGE'] = df["LOWER_AGE"].astype(int)
# now the column entries are numerical 

# same for upper age 
df['UPPER_AGE'] = df["AGEDIST"].str.extract('-(\d+)')
df['UPPER_AGE'] = df["UPPER_AGE"].astype(int)

 
"""
BUT
lower_age is still an object! because we extracted it as a string 

RangeIndex: 161 entries, 0 to 160
Data columns (total 10 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   AGE                  161 non-null    int64  
 1   ghqscore_sum         161 non-null    float64
 2   jobsatisfaction_sum  161 non-null    float64
 3   workload_sum         161 non-null    float64
 4   AGEDIST              161 non-null    object 
 5   MARITALSTATUS        161 non-null    object 
 6   CHILDREN             158 non-null    float64
 7   female               161 non-null    int64  
 8   HOURSWORKED          161 non-null    float64
 9   LOWER_AGE            161 non-null    object 
dtypes: float64(5), int64(2), object(3)
memory usage: 12.7+ KB
None
"""