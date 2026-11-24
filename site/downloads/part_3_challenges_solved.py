################################################################################
# Welcome to the challenges of Part 3!
################################################################################
# © 2024–2026 Raquel Adaia Sandoval Ortega · Python: From Lost to Boss I · https://sandovalortega.com/python-lost-to-boss-1/
# Free to reuse with credit: code under the MIT licence, course text under CC BY 4.0 (see LICENSE.txt).
# The challenges build on each other: write them all in this file and run it from the top.

# Import library at the beginning of the script
import numpy as np

############################################
# Challenge 1:
# Generate a list of the names of your 6 mice.
# Oops! You forgot two!
# Add them to the list.
# Oops again! The 6th mouse should be called m10. Correct it.
# Print the number of animals and their IDs.
############################################

mice = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6']
forgotten_mice = ['m7', 'm8']
mice = mice + forgotten_mice  # OR mice.extend(forgotten_mice)  (careful: mice.append(forgotten_mice) would add the whole list as ONE element)
mice[5] = 'm10'  # The 6th mouse is in index 5 (Python starts counting from 0)
print(f"Number of animals: {len(mice)}\nAnimal IDs: {mice}")

############################################
# Challenge 2:
# Create a matrix of 8 (animals) x 3 (time points).
# Now you have collected a new time point.
# Add it!
# You made a mistake in the 2nd animal (index 1), last time point! Set it to 0.
# Oops! You mixed the 4th animal (index 3) with the last one. Swap them!
############################################

# Create the variables containing the info about the size of the matrix
n_animals = len(mice)
n_timepoints = 3
# Generate the data
data = np.random.rand(n_animals, n_timepoints)
new_timepoint = np.random.rand(n_animals, 1)
data = np.concatenate((data, new_timepoint), axis=1)
# Do the necessary corrections
data[1, -1] = 0
data_animal4 = data[3, :].copy()  # .copy() makes an independent copy (without it, changing data would also change data_animal4)
data_animal8 = data[7, :].copy()
data[3, :] = data_animal8
data[7, :] = data_animal4
print(f"Shape of the data (animals, time points): {data.shape}")
print(np.round(data, 2))

############################################
# Challenge 3:
# Average the data of each animal.
# Print the first 3 animal names next to their averages.
############################################

average_data = np.mean(data, axis=1)
print(f"Animal: {mice[0]}, Average: {average_data[0]}")
print(f"Animal: {mice[1]}, Average: {average_data[1]}")
print(f"Animal: {mice[2]}, Average: {average_data[2]}")

# NOTE: You can use np.round() to round the values
print(f"Animal: {mice[0]}, Average: {np.round(average_data[0], 1)}")

############################################
# Challenge 4:
# Time to figure out if your treatment has worked!
# Take the first time points.
# Take the last time points.
# Are the values in the last time points larger than the first points?
# Collect and print the animals for which this is True.
############################################

# Collect the data
first_timepoints = data[:, 0]
last_timepoints = data[:, -1]
condition = last_timepoints > first_timepoints
# Convert the mouse list to an array to be able to select the mice
mice = np.array(mice)
# Select the animals that meet the condition
animals_condition = mice[condition]
# Print the result
print(f"Animals with larger values in the last time points: {animals_condition}")


############################################
# Challenge 5:
# I’ll invite you for a beer if:
#   Your treatment worked in more than 4 animals.
#   You are allowed to drink alcohol.
#   You have your ID.
# Will I invite you?
############################################

# Create the variables that will determine if you will be invited
n_animals_treatment_worked = len(animals_condition)
your_age = 18
limit_drinking = 21
allowed_to_drink = your_age >= limit_drinking
have_id = True
# Determine if you will be invited
invite = n_animals_treatment_worked > 4 and allowed_to_drink and have_id
# Print the result
# In Part 6 you will learn if/else to print a nicer sentence
print(f"The treatment worked in {n_animals_treatment_worked} animals, you are {your_age} and it is {have_id} that you have your ID.")
print(f"Will I invite you for a beer? {invite}")
