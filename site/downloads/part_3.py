#############################################################################################
# Welcome to Part 3!
###################################################################
# © 2024–2026 Raquel Adaia Sandoval Ortega · Python: From Lost to Boss I · https://sandovalortega.com/python-lost-to-boss-1/
# Free to reuse with credit: code under the MIT licence, course text under CC BY 4.0 (see LICENSE.txt).
# In this part we will learn about data structures and how to work with them.

# Remember! Anything after a "#" is a comment and will not be executed by Python.

# Import all libraries at the beginning of the script
# TODO: import the numpy library as np


############################################
# Tuple
############################################

# A tuple is a collection of items that are ordered and unchangeable.

# Create a tuple
tuple1 = ("apple", "banana", "cherry")
print(tuple1)

# This is also a tuple
tuple2 = (1, 2, 3)
print(tuple2)

# You can create a tuple with only one item by adding a comma after the item
tuple3 =
print(tuple3)

# You can mix different data types in a tuple
tuple4 =
print(tuple4)

############################################
# List
############################################

# A list is a collection of items that are ordered and changeable.
list1 = ["control", "drug1", "drug2"]
print(list1)

# You can also use the method list() to create a list


# A list with only one item: [1] works, no comma needed (unlike tuples!)
list2 = [1]
print(list2)

# This is an empty list
empty_list = []

# TODO: Try it yourself! Create a list with only one item and print it

# As with the tuple, you can mix different data types in a list
# TODO: Try it yourself! Create a list with different data types and print it

# You can change the value of a specific item in a list
idx_to_change =
new_value = "placebo"
list1[] =

# You can repeat the items in a list by multiplying the list
list2 =
print(list2)

# You can add items to a list by using the append() method
animals = ['m32', 'm33', 'm34', 'm35']
new_animal = 'm36'
# TODO: add new_animal to the list with .append()
animals
print(animals)

# You can remove items from a list by using the remove() method
animal_to_remove = 'm32'
# TODO: remove animal_to_remove from the list with .remove()
animals
print(animals)

# You can remove items from a list by using the pop() method and an index
idx_to_remove = 1
# TODO: use .pop(idx_to_remove): it removes the item AND gives it back, so you can save it in animal_removed
animal_removed = animals
print(animals)

# TODO: Add the animal you removed back to the list and print it
# TODO: Read about the insert() method and try it yourself

############################################
# Vector
############################################

# A vector is an ordered list of numbers

# You can create a vector using a list
vector1 = [1, 2, 3]
print(vector1)

# Or a tuple
vector2 = (1, 2, 3)
print(vector2)

# Let's try to modify vector1 and vector2 - What happens?

# Let's try to sum vector3 and vector4 with + . What happens? Then try with np.array()
vector3 = [4, 5, 6]
vector4 = [7, 8, 9]
vector5 =

# Let's concatenate vector3 and vector4 as arrays
# Hint: np.concatenate((array1, array2)): note the double parentheses, the arrays go inside a tuple

# Let's multiply vector3 by a scalar

############################################
# Matrix
############################################

# A matrix can be created as a list of lists
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix1)

# You can access the elements of a matrix using two indices
element = matrix1[1][1]
print(element)

# Let's sum matrix2 and matrix3
matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_sum =

# Concatenation of arrays
matrix2a = np.array(matrix2)
matrix3a = np.array(matrix3)

rows_added = np.concatenate((matrix2a, matrix3a), axis=0)  # adds rows (axis=0 is the default)
columns_added = np.concatenate((matrix2a, matrix3a), axis=1)  # adds columns
print(rows_added.shape)  # (6, 3): 6 rows, 3 columns
print(columns_added.shape)  # (3, 6): 3 rows, 6 columns

# Let's create a matrix with random values
# TODO: give np.random.rand() the number of rows and columns, e.g. np.random.rand(3, 5)
matrix_random = np.random.rand()
print(matrix_random)

# Let's create a matrix with zeros
# Hint: np.zeros((3, 5)): the shape is a tuple (rows, columns), hence the double parentheses
matrix_zeros =

# Let's create a matrix with ones
# Hint: np.ones((rows, columns)), same pattern as np.zeros
matrix_ones =

# Let's create a matrix with a specific value using np.full
# Hint: np.full((rows, columns), value)


# To create a matrix with a specific value, you can also use the np.ones() method and multiply it by the value
value = 10
matrix_value =  * value

# Let's create a matrix with a diagonal of ones (use np.eye). This is the identity matrix.
# Hint: np.eye(3) gives a 3 x 3 matrix with ones on the diagonal and zeros everywhere else
identity_matrix =

# Let's create a matrix with a specific diagonal
# np.diag(list) puts the numbers of the list on the diagonal and zeros everywhere else
diagonal = [1, 2, 3]
matrix_diag = np.diag(diagonal)

# Create a large matrix of 100 x 100 with random values
large_matrix =

# I want the number in the 2nd row and 3rd column (Python counts from 0: index [1, 2])


# I want the 3rd row of the matrix (row index 2; a ":" alone means "all the columns")


# Let's compare values of two arrays: is the 3rd row larger than the 1st row?


# I want a slice of the matrix from the 2nd to the 4th row and from the 2nd to the 4th column
# (indices 1, 2 and 3: write [1:4, 1:4], because the end of a slice is NOT included)


# Explore the dimensions of a matrix
# Hint: every array has a .shape attribute (no parentheses), e.g. matrix_zeros.shape gives (3, 5)
shape =
print(shape)

# You can also reshape a matrix as long as you keep the same number of elements (=size)
# .size is the total number of elements (rows x columns);
# np.reshape(matrix, (rows, columns)) gives the same numbers with a new shape
shape_large = large_matrix.shape
size_large = large_matrix.size
dim_1 = 10
# "//" divides and drops the decimals (100 // 3 is 33)
dim_2 =   # How many columns do you need to keep the same size?
matrix_reshaped = np.reshape(large_matrix, (dim_1, dim_2))
print(f"Original shape: {shape_large}, New shape: {matrix_reshaped.shape}")

# Matrix operations (see the Operations slides)
A = np.array([[0, 1], [2, 3]])
B = np.array([[4, 5], [6, 7]])
# TODO: compute the matrix product A @ B, the element-by-element product A * B and the transpose A.T, print them and compare

# Congratulations on finishing Part 3!! Now open part_3_challenges.py
