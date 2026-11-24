################################################################################
# Welcome to the challenges of Part 5!
################################################################################
# © 2024–2026 Raquel Adaia Sandoval Ortega · Python: From Lost to Boss I · https://sandovalortega.com/python-lost-to-boss-1/
# Free to reuse with credit: code under the MIT licence, course text under CC BY 4.0 (see LICENSE.txt).

# Import all libraries at the beginning of the script
import numpy as np
import matplotlib.pyplot as plt

# If no window appears when you run the script, uncomment these 2 lines:
# import matplotlib
# matplotlib.use('TkAgg')
# To see the figures while you debug (paused at a breakpoint), ALSO uncomment the next line,
# and change the plt.show() at the end of the script into plt.show(block=True):
# plt.ion()

# Data for the challenges ########################################################
# A sine and a cosine wave
x = np.linspace(0, 10, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# The weight (in grams) of 8 control and 8 experimental mice
weights_ctrl = np.array([29.1, 30.4, 28.7, 31.0, 29.9, 30.2, 28.5, 29.6])
weights_exp = np.array([32.3, 31.8, 33.5, 30.9, 32.7, 34.1, 31.2, 32.9])

############################################
# Challenge 1:
# Plot the sine wave.
# Make it green, 3 points wide and dashed.
# Label both axes and give the figure a title.
############################################

# Your code here


############################################
# Challenge 2:
# In a new figure, plot the sine AND the cosine waves.
# Give each line a label and add a legend.
############################################

# Your code here


############################################
# Challenge 3:
# Compare the weight of control and experimental mice:
# plot the mean of each group as a bar,
# plot each mouse as a dot on top of its bar,
# name the bars "ctrl" and "exp" and label the y axis.
############################################

# Your code here


# Show all the figures (the script waits until you close them)
plt.show()
