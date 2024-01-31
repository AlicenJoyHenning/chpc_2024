# -*- coding: utf-8 -*-
"""
Day 2 : ETL continued

CLEANING OUT DATA   

Working with dates 
General problem with dates in Excel is that formatting can be completely different 
& ideally you want to work with a date format that is consistent and clear

Most cases dates are read in as a string, even if digits with dashes 

30-01-2024 ~ british standard 
01-30-2024 ~ american assholes 

methods allows filtering of data
.str
.extract
.astype
.dt (operation)

"""

""" SECTION 1 """

import pandas as pd

df = pd.read_csv("day_02/data_02/time_series_data.csv", index_col=0)

# convert date column to date time format using pandas built in features, specifies format coming in 
df['Date'] = pd.to_datetime(df['Date'])
print(df.info)

# this is helpful because it allows more powerful features to be used with the date/time format 
df['Year'] = df['Date'].dt.year # extract year to put in new column 
df['Month'] = df['Date'].dt.month # extract month to put in new column 
df['Day'] = df['Date'].dt.day # extracts the day to put in new column 


""" SECTION 2 """
df = pd.read_csv("day_02/data_02/patient_data_dates.csv", index_col=0, )

# If not adjusted since we already have column for index we can drop the automatically generated one as it is redundant 
# df.drop(["Index"], inplace=True, axis=1)

"""
Problems 
0. redundant index column 
1. na value in date and calories columns 
2. date format 


"""
# convert to date 
df["Date"] = pd.to_datetime(df["Date"], format="mixed")
# ignore problem row in date

# still wrong : 
df.drop(index=26, inplace=True)
df.drop(index=22, inplace=True)

df["Date"] = pd.to_datetime(df["Date"])

# FILLNA : replacing empty values
# Either get the average of a column and fill the empty values 

avg_cal = df["Calories"].mean()
df["Calories"].fillna(avg_cal, inplace = True) # inplace = True 

""" EDITING DATA """

pd.set_option('display.max_rows', None)

# 1 Removing empty cells 
df.dropna(inplace = True)

# ALSO need to redo the index after removing rows 
df = df.reset_index(drop = True)


# 2 Removing duplicates DROP_DUPLICATES()
# df.drop(7, inplace = True) # possible for smaller datasets, not so much larger ones 
df.drop_duplicates(inplace = True)
df = df.reset_index(drop = True)

# 3 Outlier likely typo, changes specific value 
df.loc[7, "Duration"] = 45
 # OR explicitly for one @ a time 
# df["Duration"] = df["Duration"].replace([450], [45])
 
print(df)
# to show all columns 
# pd.set_option('display.max_rows', None)












