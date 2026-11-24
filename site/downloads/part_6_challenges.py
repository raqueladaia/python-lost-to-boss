################################################################################
# Welcome to the challenges of Part 6!
################################################################################
# © 2024–2026 Raquel Adaia Sandoval Ortega · Python: From Lost to Boss I · https://sandovalortega.com/python-lost-to-boss-1/
# Free to reuse with credit: code under the MIT licence, course text under CC BY 4.0 (see LICENSE.txt).

# Set a breakpoint at the print() before the challenges begin to generate the
# two DataFrames.

# First step: import all libraries
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# If no window appears when you run the script, uncomment these 2 lines:
# import matplotlib
# matplotlib.use('TkAgg')
# To see the figures while you debug (paused at a breakpoint), ALSO uncomment the next line,
# and change the plt.show() at the end of the script into plt.show(block=True):
# plt.ion()

# Second step: We will create DataFrame 1 #####################################

# Define the number of rows we want in the DataFrame
n_rows = 50  # You can change this number to generate more or less data

# Define which columns we are going to have
columns = ['animal', 'sex', 'experimental_condition', 'weight']

# Generate a list of mouse names (a list comprehension, see the For loops slide)
mice = [f'm{i+1}' for i in np.arange(n_rows)]

# We are going to randomly assign sex to our mice
# 1. Generate random 1s and 2s
random_numbers = np.random.randint(low=1, high=3, size=n_rows)  # high=3 is NOT included, so we get 1 or 2
# 2. Assign F to 1, and M to 2
is_1 = random_numbers == 1
is_2 = random_numbers == 2
# dtype=object: otherwise numpy would cut every text we put in this array to 4 characters (the length of 'none')
sexes = np.array(['none'] * n_rows, dtype=object)
sexes[is_1] = 'F'
sexes[is_2] = 'M'  # OR sexes[~is_1] = 'M'  --> use "~" to invert an array of booleans

# We are going to assign the experimental condition
# 1. We want to have a 50/50 distribution
n_exp = n_rows // 2  # We use "//" to ensure the result is an integer
n_ctrl = n_rows - n_exp
# 2. Generate experimental and control labels
label_exp = ['exp'] * n_exp
label_ctrl = ['ctrl'] * n_ctrl
exp_conds = label_exp + label_ctrl

# Generate random weights for our mice
# 1. Generate random numbers from a normal distribution
# [values are centered around zero, thus we have positive and negative]
random_numbers = np.random.randn(n_rows)
# 2. We are going to assume the average weight of a mouse to be 30 grams
avg_weight = 30
random_weights = random_numbers + avg_weight
# 3. We don't need so many decimals, so we will round to 2 decimals.
random_weights = np.round(random_weights, 2)

# Fill the DataFrame by column
df1 = pd.DataFrame()
df1['animal'] = mice
df1['sex'] = sexes
df1['experimental_condition'] = exp_conds
df1['weight'] = random_weights

# Third step: We will create DataFrame 2 #####################################
n_animals = 20
n_conditions = 2
condition_names = ['ctrl', 'exp']
animals = [f'm{i+1}' for i in np.arange(n_animals)]
conditions = np.array(sorted(np.random.choice(condition_names, size=n_animals)))

# Generate a timeline of 6 points in time (in days) that stays constant (around 10)
# for ctrl and drops (from around 10 to around 5) for exp after the first timepoint
# Define the number of timepoints
n_timepoints = 6

# Define the number of animals in each condition
n_ctrl = np.sum(conditions == 'ctrl')
n_exp = n_animals - n_ctrl

# Generate the data for the control animals
data_ctrls = np.zeros((n_ctrl, n_timepoints)) + np.nan
for i in range(n_ctrl):
    data_ctrls[i] = np.random.randn(n_timepoints) + 10

# Generate the data for the experimental animals
data_exps = np.zeros((n_exp, n_timepoints-1)) + np.nan
for i in range(n_exp):
    data_exps[i] = np.random.randn(n_timepoints-1) + 5

# Create a first timepoint of the experimental animals to be different
t0 = np.random.randn(n_exp) + 10

# Expand dimensions of t0 to concatenate it with data_exps
t0 = np.expand_dims(t0, axis=1)
# Set t0 as the first timepoint for exp animals using concatenation
data_exps = np.concatenate((t0, data_exps), axis=1)

# Concatenate the data for both conditions
data_all = np.concatenate((data_ctrls, data_exps), axis=0).tolist()

# Save this data in a DataFrame:
# one row per animal; the 'timeline' column holds a list of 6 values
df2 = pd.DataFrame({'animal': animals,
                    'experimental_condition': conditions,
                    'timeline': data_all})

# Set a breakpoint here to generate the two DataFrames
print()

############################################
# Challenge 1:
# For df1 → Use a for loop to
# Collect data of each experimental group
# Compute the mean
# Plot the mean as a bar plot
# Plot the individual animals as dots
############################################

# Your code here


############################################
# Challenge 2:
# For df2 → Use a for loop over the experimental conditions to:
# Collect the timelines of the animals of that condition.
# Plot each animal's timeline as a line.
# Use different colors for exp & ctrl.
# Plot the mean of each condition.
############################################

# Your code here


# Show all the figures (the script waits until you close them)
plt.show()
