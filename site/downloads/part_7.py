################################################################################
# Welcome to Part 7!
################################################################################
# © 2024–2026 Raquel Adaia Sandoval Ortega · Python: From Lost to Boss I · https://sandovalortega.com/python-lost-to-boss-1/
# Free to reuse with credit: code under the MIT licence, course text under CC BY 4.0 (see LICENSE.txt).
# In this part we will learn how to open Excel and CSV files and you will apply everything
# you have learned in the previous parts.

# Import all libraries
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# If no window appears when you run the script, uncomment these 2 lines:
# import matplotlib
# matplotlib.use('TkAgg')
# To see the figures while you debug (paused at a breakpoint), ALSO uncomment the next line,
# and change the plt.show() at the end of the script into plt.show(block=True):
# plt.ion()

# Open the data file
# (the folder "example_data" must be inside the folder you run the script from: your repository)
folder = "example_data"
filepath_data = os.path.join(folder, "data.xlsx")
df = pd.read_excel(filepath_data, engine="openpyxl")

# The same data saved as a CSV file opens with read_csv:
df_csv = pd.read_csv(os.path.join(folder, "data.csv"))
print(f"data.xlsx has {df.shape[0]} rows and {df.shape[1]} columns; data.csv has {df_csv.shape[0]} rows and {df_csv.shape[1]} columns")

# Open the metadata file
filepath_metadata = os.path.join(folder, "metadata.xlsx")
df_metadata = pd.read_excel(filepath_metadata, engine="openpyxl")

# TODO: Take a moment to explore the DataFrames: shape, columns, content....

# We are going to add the info of the metadata (sex and group of each mouse) into the data DataFrame.
# First, we create two dictionaries (mouse -> sex and mouse -> group) with a dictionary comprehension
# (like the list comprehension from Part 6). iterrows() gives you the rows of a DataFrame one by one.
dict_sex = {r['mouse']: r['gender'] for _, r in df_metadata.iterrows()}
dict_group = {r['mouse']: r['group'] for _, r in df_metadata.iterrows()}
# Now we create the new columns: .map() looks up each mouse in the dictionary
df['sex'] = df['mouse'].map(dict_sex)
df['experimental_group'] = df['mouse'].map(dict_group)

# Now we are ready for the challenges!

############################################
# Challenge 1:
# Explore the dataset by printing
# (how many and unique values):
# Experimental groups
# Sexes
# Time points
# Mouse IDs
############################################

# Your code here


############################################
# Challenge 2:
# Take the time point at day 7.
# Use a bar plot to compare experimental groups.
# Extra points: plot individual animal data,
# and differentiate males from females using different markers
############################################

# Your code here


############################################
# Challenge 3:
# For each animal:
# Collect the data of all time points
# Plot the data as a line plot
# Save the data in an array
# NOTE: color by experimental group
############################################

# Your code here


############################################
# Challenge 4:
# Within the previous figure:
# Plot the mean of each group.
# Give a legend to the figure.
# Make it beautiful! Title, labels to axes…
############################################

# Your code here


# Show all the figures (the script waits until you close them)
plt.show()
