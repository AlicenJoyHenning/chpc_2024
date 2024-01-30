""" 
STORING DATA IN PYTHON 

Looking at data storage forms to work with in Python, namely : 

1. Lists 
2. Dictionaries 
3. Data frames (NB associated with pandas)

"""
import pandas
file = pandas.read_csv("country_data.csv")

# Could enter values indiviudally to store as a variable  
# B1 = 30 
# B2 = 40 
# B3 = 30 
# B4 = 49 

# 1. Or preferably do it in a different form known as a LIST (one variable with many things in it)
# SQUARE BRACKETS ~ LIST FORMAT 

age = [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39] 
gender = ["M","M", "F", "M", "F", "F", "F", "M", "M", "F", "M"]
country = ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"] 
print(age)

"""
OUTPUT: 
[30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39]
"""


"""
1. LIST NOTES 

print(age[0]) # Note : indexing - age[index] - starts at 0 for lists 
print(gender[-1]) # Note : you can access the last value in the list using -1 

# We can use built in Python functions to get statistics on this list 
min_age = min(age) 22
max_age = max(age) 49
len_age = len(age) 11
sum_age = sum(age) 
average = sum_age / len_age

Lists can store all kinds of data types and many things can be done with them 
> print all items in the list [:]
my_list = [42, -2021, 6.283, 'tau', 'node']
print(my_list[:])

> we can add items to the end of lists using append()
my_list.append("pi")
print(my_list)

> add items @ specific positions using insert()
my_list.insert(1, "pi2")

> remove an item from the list using removal()
my_list.remove("tau")

"""

print(age[0:2])
# OUTPUT [30, 40] does to position n-1 

print(age[0:3])
# OUTPUT [30, 40 ,50] 

age.append(100)
print(age)
# OUTPUT [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39, 100]


"""
2. Dictionaries 

Collection of key-value pairs, where each key is unique (aka associative arrays) similar to lists but instead of using integer indices to access elements, you can use keys. 
It is an unordered data type that is structured using keys and values & is defined with curly brackets {} 

E.g: cat : "a cute animal"
Has some value, 'cat' and some association 'a cute animal'
BUT 
it doesn't have indices, unordered

DICTIONARY : CURLY BRACKETS
"""

# SYNTAX
d = {'key1' : 'value1', 'key2':'value2'}

person = {'name':'John Doe', 
          'age':30,
          'address':'123 Main St.'}
print(person['name'])
# OUTPUT : John Doe 
print(person.get('age'))
# OUTPUT : 30 
print(person.get('age'))
# OUTPUT : 30 
person['phone'] = '555-555-555' 
 
# Creating a dictionary called 'mammals'
mammals = {'cat':'a cute animal',
           'lion':'king of the jungle',
           'elephant':'a gigantic herbivore'}

# Now to access specific information 
print(mammals["cat"])
# OUTPUT : a cute animal

"""
3. Data Frames 

When dealing with tabular data, the pandas library provides a versatile data structure called a DataFrame
This is a 2D, labelled data structure with columns that can be of different types like a spreadsheet or SQL table 
For this example we will convert the previous lists into a Pandas DataFrame to demonstrate its advantages  
(exactly like in R)
(SeeQuill > SQL ... not 'S' 'Q' 'L')
"""

import pandas as pd

# Create a DataFrame where df refers to data frame 
data = {
        'age' : [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39] ,
        'gender' : ["M","M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
        'country' : ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
        }

df = pd.DataFrame(data) # importing as 'pd' means we don't have to write out 'pandas' each time 
print(df)

# ADVANTAGES OF DFs 
# 1. Access specific columns 
print(df['age'])
""" 
OUTPUT : 
0     30
1     40
2     30
3     49
4     22
5     35
6     22
7     46
8     29
9     25
10    39
"""

# 2. Descriptive statistics 
print(df['age'].min()) # OUTPUT : 22
print(df['age'].max()) # OUTPUT : 49 
print(df['age'].mean()) # OUTPUT : 33.36

# 3. Filtering and slicing based on conditions is simplified 
print(df[df['age'] > 30])
"""
    age gender       country
1    40      M      Botswana
3    49      M  South Africa
5    35      F    Mozambique
7    46      M         Kenya
10   39      M         Sudan

"""
print(df[1:4]) # selects rows 1 to 3 

"""
   age gender       country
1   40      M      Botswana
2   30      F  South Africa
3   49      M  South Africa

"""

# 4. Flexibility : allows easy addition or removal of columns 
df['new_column'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(df)
"""

    age gender       country  new_column
0    30      M  South Africa           1
1    40      M      Botswana           2
2    30      F  South Africa           3
3    49      M  South Africa           4
4    22      F         Kenya           5
5    35      F    Mozambique           6
6    22      F       Lesotho           7
7    46      M         Kenya           8
8    29      M         Kenya           9
9    25      F         Egypt          10
10   39      M         Sudan          11
"""

df.drop(columns = ['new_column'], inplace=True)
print(df)
"""
    age gender       country
0    30      M  South Africa
1    40      M      Botswana
2    30      F  South Africa
3    49      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    46      M         Kenya
8    29      M         Kenya
9    25      F         Egypt
10   39      M         Sudan
"""


# Class example for a data frame 

fruits = ["apple", "banana", "orange", "grape","kiwi"]
size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_sizes = {'fruits' : fruits, 'sizes' : size_nm}

df = pd.DataFrame(fruit_sizes)
print(df['fruits'])

"""
0     apple
1    banana
2    orange
3     grape
4      kiwi
"""

print(df['sizes'].min()) # 8.7
print(df.describe())

"""
OUTPUT
           sizes
count   5.000000
mean   12.460000
std     4.795102
min     8.700000
25%     9.800000
50%    10.100000
75%    13.200000
max    20.500000
"""

# Filter (can also be done for categorical data)
print(df[df['sizes'] > 10])
"""
OUTPUT
   fruits  sizes
1  banana   10.1
2  orange   13.2
4    kiwi   20.5
"""

print(df[1:3]) # gives a range of rows, again like lists give you up to n-1
"""
OUTPUT
   fruits  sizes
1  banana   10.1
2  orange   13.2

"""

prices = [10.00, 12.50, 16.00, 23.00, 7.00]

df['prices'] = prices # adds a column 

df.drop(columns=['sizes'], inplace=True) # removes added column 

