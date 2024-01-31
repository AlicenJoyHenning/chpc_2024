"""
ETL : Applying data transformations 

Using pandas to do things like merging files (append and merge) 

"""

""" SECTION 1 """

import pandas as pd 

df = pd.read_csv("day_02/data_02/iris.csv")

# How to extract headers from a dataframe (so you don'ts have to open and look at it)
col_names = df.columns
col_names = df.columns.tolist()
print(col_names)

"""
['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
"""

# Create another column with square value of a current column 
df["sepal_length_sq"] = df["sepal_length"]**2
# more complex methods this will be easier / custom function to each entry of a column 
df["sepal_length_sq"] = df["sepal_length"].apply(lambda x: x**2)

# Grouping by categories 
grouped = df.groupby("class")
# to calculate mean based on groups 
mean_sq = grouped["sepal_length_sq"].mean()

"""
OUTPUT : works out mean on groups in a column 

class
Iris-setosa        25.1818
Iris-versicolor    35.4972
Iris-virginica     43.7980
Name: sepal_length_sq, dtype: float64

"""

# Working with multiple files 

df1 = pd.read_csv("day_02/data_02/person_split1.csv")
df2 = pd.read_csv("day_02/data_02/person_split2.csv")

# add them, make a list with one df after the other in one 
df = pd.concat([df1, df2], ignore_index=True)

# files with different column names (relationship btw df )

df_1 = pd.read_csv("day_02/data_02/person_education.csv")
df_2 = pd.read_csv("day_02/data_02/person_work.csv")

# inner join to merge together the above, here is an inner join, 
df_merge_inner = pd.merge(df_1, df_2, on="id") # specifies the relationship is the "id" column

# different parameters of merge (default is inner)

# outer join : if no match 'nas' everywhere else   
df_merge_outer = pd.merge(df_1, df_2, )



""" SECTION 2 """

df = pd.read_csv("day_02/data_02/country_data_index.csv")

# Filtering data 
# example based on 'age' column 
print(df[df['Age'] > 30])

"""
OUTPUT: 
    
   Unnamed: 0  Age Gender       Country
0           0   39      M  South Africa
3           3   46      M  South Africa
5           5   35      F    Mozambique
7           7   49      M         Kenya
9           9   40      F         Egypt

"""

# using the iris dataset 
df = pd.read_csv("day_02/data_02/iris.csv")

# CLEANING Here the class column can be adjusted, they all have 'Iris_' 
# df['class'] = df['class'].str.extract('-(\.)')
df["class"] = df["class"].str.replace("Iris-", "")

# Now for FILTERING 
# Give rows where sepal length > 5 
df = df[df["sepal_length"] > 5]

# only see data for virginica 
df = df[df["class"] == "virginica"]


""" SECTION 3 """
# LOAD : exporting the data, or sending the data somewhere 

# to export to separate folder : note pandas doesn't create a directory 
df.to_csv("day_02/output/virginica_filtered.csv")

url = "https://raw.githubusercontent.com/alexandrehsd/Predicting-Pulsar-Stars/master/pulsar_stars.csv"

df = pd.read_csv(url)
















