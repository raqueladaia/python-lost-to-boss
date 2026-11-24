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

# Collect the information
group_types = np.unique(df['experimental_group'])
sexes = np.unique(df['sex'])
time_points = np.unique(df['Timepoint_SNI_day'])
mouse_ids = np.unique(df['mouse'])

# Count how many unique values we have for every variable we have collected
n_group_types = group_types.shape[0]
n_sexes = sexes.shape[0]
n_time_points = time_points.shape[0]
n_mouse = mouse_ids.shape[0]

# Transform the information into strings to print it nicely
# ', '.join(...) only accepts text: .astype(str) converts the numbers (time points, mouse IDs) into text first
group_types_print = ', '.join(group_types.astype(str))
sexes_print = ', '.join(sexes.astype(str))
time_points_print = ', '.join(time_points.astype(str))
mouse_ids_print = ', '.join(mouse_ids.astype(str))

# Print the information
print(
    "We have:"
    f"\n\t{n_group_types} groups: {group_types_print}"
    f"\n\t{n_sexes} sexes: {sexes_print}"
    f"\n\t{n_time_points} time points: {time_points_print}"
    f"\n\t{n_mouse} mice: {mouse_ids_print}"
)

############################################
# Challenge 2:
# Take the time point at day 7.
# Use a bar plot to compare experimental groups.
# Extra points: plot individual animal data,
# and differentiate males from females using different markers
############################################

# Collect the information for day 7 post-SNI
seven = df['Timepoint_SNI_day'] == 7
df_seven = df[seven]

# Collect the experimental groups that you have for this time point
# You can omit this step if you know that you have the same
# experimental groups throughout your whole experiment and you
# have collected this info before (e.g. in challenge 1)
exp_groups = np.unique(df['experimental_group'])

# Define which colors you want for each experimental group
colors = {'control': 'blue',
          'experimental': 'red'}

# Use a for loop to iterate over the experimental groups
# and plot the data as a bar plot and scatter plot in a figure
fig = plt.figure()  # Initialize the figure
for i, ec in enumerate(exp_groups):
    condition_ec = df_seven['experimental_group'] == ec
    df_condition = df_seven[condition_ec]
    vals = df_condition['threshold_50']
    n_vals = vals.shape[0]
    means = np.mean(vals)
    sem = np.std(vals, ddof=1) / np.sqrt(len(vals))  # ddof=1: sample standard deviation
    print(f"Day 7, {ec}: mean = {means:.3f} g, SEM = {sem:.3f} g ({n_vals} mice)")
    plt.bar(i, means, color=colors[ec], yerr=sem)
    # The up-down method gives only a limited set of values, so two mice can have exactly the same value
    # and their dots would fall exactly on top of each other.
    # np.linspace(-0.1, 0.1, n_vals) spreads the dots a little to the left and right of the bar centre (i)
    xax_scatter = i + np.linspace(-0.1, 0.1, n_vals)
    plt.scatter(xax_scatter, vals, color='white', edgecolor='black')
# Name the bars and the axes
plt.xticks(range(len(exp_groups)), exp_groups)
plt.ylabel('50% withdrawal threshold (g)')
plt.title('Day 7 after surgery')

# If you want to differentiate males from females you can add
# a for loop within the existing for loop like this:
# First, define a new dictionary where you assign different markers
# to each sex
markers = {'female': '^',
           'male': 'o'}
# Initialize the figure
fig = plt.figure()
# The first for loop separates experimental conditions
for i, ec in enumerate(exp_groups):
    condition_ec = df_seven['experimental_group'] == ec
    df_condition = df_seven[condition_ec]
    vals = df_condition['threshold_50']
    means = np.mean(vals)
    sem = np.std(vals, ddof=1) / np.sqrt(len(vals))
    plt.bar(i, means, color=colors[ec], yerr=sem)

    # The second for loop within the first for loop separates sexes
    for sex in sexes:
        df_sex = df_condition[df_condition['sex'] == sex]
        vals = df_sex['threshold_50']
        n_vals = vals.shape[0]
        # Spread the dots a little, as in the first figure. But np.linspace(-0.1, 0.1, 1) gives [-0.1],
        # so a group with a single mouse would be drawn off-centre: np.zeros(1) puts it in the centre instead
        offsets = np.linspace(-0.1, 0.1, n_vals) if n_vals > 1 else np.zeros(1)
        xax_scatter = i + offsets
        # Give each sex a label only once (in the first group), so the legend does not repeat it
        if i == 0:
            label = sex
        else:
            label = None
        plt.scatter(xax_scatter, vals, color='white', edgecolor='black', marker=markers[sex], label=label)
# Name the bars and the axes, and add the legend
plt.xticks(range(len(exp_groups)), exp_groups)
plt.ylabel('50% withdrawal threshold (g)')
plt.title('Day 7 after surgery')
plt.legend(loc="upper left")  # place the legend where it does not hide any dot

############################################
# Challenge 3:
# For each animal:
# Collect the data of all time points
# Plot the data as a line plot
# Save the data in an array
# NOTE: color by experimental group
############################################

# Count how many mice we have in each experimental group
n_in_group = {}
for g in group_types:
    mice_in_group = np.unique(df[df['experimental_group'] == g]['mouse'])
    n_in_group[g] = mice_in_group.shape[0]

# Create one empty array (mice x time points) for each experimental group
# to store the data (this is to prepare the data for challenge 4)
data_challenge4 = {}
for g in group_types:
    data_challenge4[g] = np.zeros((n_in_group[g], n_time_points)) + np.nan

# Keep track of the next free row in the array of each group (we start at row 0)
next_row = {}
for g in group_types:
    next_row[g] = 0

# Define which colors you want for each experimental group
colors = {'control': 'blue',
          'experimental': 'red'}

# Initialize the figure
plt.figure()

# Iterate over the mouse IDs to collect their data
for m in mouse_ids:
    # Collect the information for the mouse, sorted by time
    df_m = df[df['mouse'] == m].sort_values('Timepoint_SNI_day')
    # Collect to which experimental group the mouse belongs to (it is the same in all its rows)
    ec = df_m['experimental_group'].values[0]
    # Collect all the values
    vals = df_m['threshold_50'].values
    # Save the values in the next free row of the array of its group
    row = next_row[ec]
    data_challenge4[ec][row, :] = vals
    next_row[ec] = row + 1
    # Plot the data for that mouse
    plt.plot(df_m['Timepoint_SNI_day'], vals, color=colors[ec], linewidth=0.5, alpha=0.3)

# Check the arrays
for g in group_types:
    print(f"{g}: array of {data_challenge4[g].shape[0]} mice x {data_challenge4[g].shape[1]} time points")

############################################
# Challenge 4:
# Within the previous figure:
# Plot the mean of each group.
# Give a legend to the figure.
# Make it beautiful! Title, labels to axes…
############################################

# Plot the mean within the previous figure for each experimental condition
for ec in group_types:
    vals = data_challenge4[ec]
    mean = np.mean(vals, 0)  # 0: average over the mice (rows), one mean per time point
    print(f"{ec}, mean per time point: {np.round(mean, 2)}")
    plt.plot(time_points, mean, label=ec, color=colors[ec], linewidth=2)

# Give a legend to the figure
plt.legend()

# Make the figure beautiful!
# 1. Set x ticks to meaningful values
plt.xticks(time_points)
# 2. Provide a label to the x axis
plt.xlabel('Time (days)')
# 3. Provide a label to the y axis
plt.ylabel('Mechanical threshold of the left hind paw (g)')
# 4. Give a title to the figure
plt.title('Mechanical sensitivity before and after SNI')
# 5. Indicate at what time the injury to evoke chronic pain
# was executed.
plt.axvline(0, color='black', linestyle='--')
# 6. Despine the graph for visual purposes
sns.despine()
# After plotting I decided I wanted to give the ticks to
# the y axis to avoid an overcrowded axis
yticks = np.linspace(0, 1.6, 5)
plt.yticks(yticks)

print('DONE! :)')

# Show all the figures (the script waits until you close them)
plt.show()
