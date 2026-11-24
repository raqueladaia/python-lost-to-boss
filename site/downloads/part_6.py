################################################################################
# Welcome to Part 6!
################################################################################
# © 2024–2026 Raquel Adaia Sandoval Ortega · Python: From Lost to Boss I · https://sandovalortega.com/python-lost-to-boss-1/
# Free to reuse with credit: code under the MIT licence, course text under CC BY 4.0 (see LICENSE.txt).
# In this part we will learn about flow control: if/elif/else, for loops and while loops.

# Import all libraries at the beginning of the script
import numpy as np
import matplotlib.pyplot as plt

# If no window appears when you run the script, uncomment these 2 lines:
# import matplotlib
# matplotlib.use('TkAgg')
# To see the figures while you debug (paused at a breakpoint), ALSO uncomment the next line,
# and change the plt.show() at the end of the script into plt.show(block=True):
# plt.ion()

# If statements
x = 10
y = 100

# TODO: Write an if / elif / else that prints whether x is smaller than,
# equal to, or larger than y. Then change the values of x and y and run it again.


print("Now it's out of if statement")

# For loops
for i in np.arange(10):
    print(i)

# List comprehension: a for loop written inside a list, in one line
list1 = [f'm{i}' for i in range(10)]

# For loop with enumerate: gives you the index AND the element at each iteration
for i, mouse in enumerate(list1):
    print(f'In index {i}, there is mouse {mouse}')


# How to use enumerate to create a figure with multiple conditions
plt.figure()
conditions = ['condition1', 'condition2', 'condition3']
colors = ['blue', 'purple', 'cyan']

for i, cond in enumerate(conditions):
    data = np.random.rand(10) * (i + 1)  # parentheses matter: without them, the data is multiplied by i and THEN 1 is added
    meandata = np.mean(data)
    sem = np.std(data, ddof=1) / np.sqrt(len(data))  # ddof=1: sample standard deviation
    # TODO: plot meandata as a bar at position i, with the SEM as error bar (yerr) and the color of this condition

    plt.scatter([i] * len(data), data, color='white', edgecolor='black')


# You can also iterate over a list
list_of_animals = ['mouse1', 'mouse2', 'mouse3']
for animal in list_of_animals:
    print(animal)

# While loops
i = 0
while i < 10:
    print(f'Inside while loop - Iteration {i}')
    i += 1

print('We are outside of the while loop')

# You can also use continue if a condition is met to skip the rest of the loop 
# and go to the next iteration
for i in range(10):
    if i == 5:
        print('i = 5, skipping')
        continue
    print(i)

# Show all the figures (the script waits until you close them)
plt.show()

# Congratulations on finishing Part 6! Now open part_6_challenges.py
