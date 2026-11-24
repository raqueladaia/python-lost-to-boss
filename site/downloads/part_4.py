################################################################################
# Welcome to Part 4!
################################################################################
# © 2024–2026 Raquel Adaia Sandoval Ortega · Python: From Lost to Boss I · https://sandovalortega.com/python-lost-to-boss-1/
# Free to reuse with credit: code under the MIT licence, course text under CC BY 4.0 (see LICENSE.txt).
# In this part we will learn about Dictionaries and DataFrames.

# Import all libraries at the beginning of the script
import numpy as np  # This library will allow us to do operations on our data
import pandas as pd  # This library will allow us to generate and work with DataFrames

# REMEMBER: To run the code in Debug mode, set a breakpoint next to a line of code (no comments, no empty lines).
# Python will only run the instructions before the breakpoint.
# But if any line has a syntax error (e.g. an unfinished `x =`), nothing runs at all:
# comment out the unfinished lines first.
# In scripts that contain errors, like this one, you want to comment out all lines after the breakpoint.
# To comment out selected lines:
#           Windows:    Ctrl + /
#           macOS:      Cmd + /

############################################
# Dictionaries
############################################

# This is how we create empty dictionaries
dict_1 = {}
dict_2 = dict()  # dict() is a built-in function: DO NOT name a variable "dict", or you will hide it

# To add data into dictionaries, we need keys and values.
# If you have already created an empty dictionary, you can fill it like this:
dict_1['animal'] = 'm33'
dict_1['sex'] = 'male'
dict_1['experimental_group'] = 'ctrl'

# If you are creating a dictionary from scratch, do it this way:
dict_3 = {'animal': 'm34',
          'sex': 'male',
          'experimental_group': 'exp'}

# Now we are going to create a nested dictionary.
# Hint: a nested dictionary is a dictionary whose values are dictionaries (use dict_1 and dict_3)
dict_2 =

# Let's access values in dict_1
# Hint: dict_1['key'] gives you the value of that key
dict_1[]

# Let's access values in nested dictionary
# Hint: use two keys in a row: dict_2['first_key']['second_key']
dict_2

# Retrieve all keys of dict_3
# Hint: use the .keys() method
keys_dict_3 =


# Retrieve all values
all_values = dict_1.values()
print(list(all_values))

# Retrieve all items (key-value pairs)
# Hint: use the .items() method
all_items =

# Add more information to dict_1
# Hint: create a new dictionary and add it to dict_1 with the .update() method
new_info = {

# Add more information to nested dictionary
# Hint: add a new key to dict_2 whose value is a new dictionary


# Remove a key and its value from dict_1 using the pop() method
key_to_remove =
removed_item =

############################################
# DataFrames
############################################

# You need the pandas library to create a DataFrame
df_empty_1 = pd.DataFrame()

# You can create a DataFrame that is empty but whose columns are defined
columns = ['animal', 'sex', 'experimental_condition', 'weight']
df_empty_2 = pd.DataFrame(columns=columns)

# Create a DataFrame called df with at least 7 mice (ctrl and exp, M and F): the rest of the script uses it

# We can fill the DataFrame in multiple ways

# Line by line
# Hint: df.loc[0] = [...] adds a row with index 0 (one value per column)


# Column by column
# Hint: df['column_name'] = [...] adds a whole column (one value per row)


# All at once
# Hint: pd.DataFrame(list_of_rows, columns=columns), where each row is a list


# Using dictionaries
# Hint: pd.DataFrame({'column_name': [values], ...}): each key becomes a column


# Investigating your DataFrame
# ... what is the size of your DataFrame?
# Hint: .shape

# ... what are the columns?
# Hint: .columns

# ... and the indices?
# Hint: .index

# ... which are the unique values you have?
# Hint: df['column_name'].unique()


# How to add/remove....
# ... a column
# Hint: add it like in "Column by column", remove it with df.drop(columns=[...])

# ... a row
# Hint: add it with df.loc[new_index] = [...], remove it with df.drop(index=...)

# What happened to the indices?


# Accessing rows in the DataFrame
# Hint: .iloc[] looks for the POSITION of the row, .loc[] looks for its LABEL (the index)
# Compare df.iloc[3] and df.loc[3] after removing a row: are they the same mouse?


# Renumber the indices from 0
# Hint: .reset_index(drop=True) (drop=True throws away the old indices)


# Collecting information of interest
# ... using booleans
col_of_interest = 'experimental_condition'
info_of_interest = 'ctrl'
# Hint: df[col] == value gives you True/False for every row; use it inside df[...] to keep the True rows


# ... using queries
df_ctrl = df.query('experimental_condition == "ctrl"')
df_exp = df.query('experimental_condition == "exp"')

# Operations of values in a column
col = 'weight'
# Hint: df[col].mean(), .max(), .min(), .std()...


# More operations on the df data
# Hint: df.groupby('column')[col].mean() computes the mean of each group; df.describe() summarizes everything


############################################
# Challenges
############################################

# Open the document part_4_challenges.py to complete the challenges.
