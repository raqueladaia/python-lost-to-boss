################################################################################
# Welcome to Part 5!
################################################################################
# © 2024–2026 Raquel Adaia Sandoval Ortega · Python: From Lost to Boss I · https://sandovalortega.com/python-lost-to-boss-1/
# Free to reuse with credit: code under the MIT licence, course text under CC BY 4.0 (see LICENSE.txt).
# In this part we will learn how to plot your data.

# Import all libraries at the beginning of the script
import numpy as np  # This library will allow us to do operations on our data
import pandas as pd  # This library will allow us to work with DataFrames (Part 4)
import matplotlib.pyplot as plt  # This library will allow us to plot our data
import seaborn as sns  # This library will allow us to plot our data in a more visually appealing way

# If no window appears when you run the script, uncomment these 2 lines:
# import matplotlib
# matplotlib.use('TkAgg')
# To see the figures while you debug (paused at a breakpoint), ALSO uncomment the next line,
# and change the plt.show() at the end of the script into plt.show(block=True):
# plt.ion()

# REMEMBER: To run the code in Debug mode, set a breakpoint next to a line of code (no comments, no empty lines).
# Python will only run the instructions before the breakpoint.
# But if any line has a syntax error (e.g. an unfinished `x =`), nothing runs at all:
# comment out the unfinished lines first.
# In scripts that contain errors, you want to comment out all lines after the breakpoint.
# To comment out selected lines:
#           Windows:    Ctrl + /
#           macOS:      Cmd + /

############################################
# Scatter plots: two measurements per item (x vs y)
############################################

x = np.random.rand(10)
y = np.random.rand(10)

# Every new figure starts with plt.figure()
plt.figure()
plt.scatter(x, y)

############################################
# Bar plots: average your data and plot it as a single bar
############################################

values_g1 = np.random.rand(10)
values_g2 = np.random.rand(10) + 0.5

# TODO: compute the mean of each group
group1_avg =
group2_avg =

# TODO: plot both means as bars at the x positions 0 and 1 in a NEW figure


# Plot the individual values as dots on top of each bar.
# Every dot of group 1 goes at x = 0, every dot of group 2 at x = 1
plt.scatter([0] * 10, values_g1, color='white', edgecolor='black')
# TODO: do the same for group 2


############################################
# Line plots: values along an ordered axis such as time
############################################

x = np.linspace(0, 10, 100)  # 100 points between 0 and 10
y = np.sin(x)

plt.figure()
plt.plot(x, y)

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Sine wave')

############################################
# Seaborn
############################################

# Seaborn is built on top of matplotlib. Many of its functions accept a DataFrame directly:
# you give it the DataFrame (data=...) and the NAMES of the columns to plot (x=..., y=...).
# Let's build a small DataFrame (like in Part 4) with the weight of 8 ctrl and 8 exp mice
df = pd.DataFrame({'group': ['ctrl'] * 8 + ['exp'] * 8,
                   'weight': [29.1, 30.4, 28.7, 31.0, 29.8, 30.2, 28.9, 30.6,
                              31.8, 32.5, 30.9, 33.1, 32.0, 31.4, 33.6, 32.2]})

plt.figure()
# sns.barplot() computes the mean of each group for you (the dark line on each bar is the 95% confidence interval)
# capsize=0.2 adds small horizontal caps to that line, so it is easier to see
sns.barplot(data=df, x='group', y='weight', capsize=0.2)
# TODO: add the individual mice on top of the bars with sns.stripplot (same data, x and y, color='black', alpha=0.6 and zorder=1.5)
# alpha=0.6 makes the dots a bit transparent; zorder decides what is drawn on top: the bars have zorder 1 and
# the confidence interval line zorder 2, so zorder=1.5 puts the dots above the bars but below the line


# sns.despine() removes the top and right borders of the current figure
sns.despine()

# Show all the figures (the script waits until you close them)
plt.show()

# Congratulations on finishing Part 5! Now open part_5_challenges.py
