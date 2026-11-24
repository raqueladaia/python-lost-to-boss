################################################################################
# Welcome to Part 1!
################################################################################
# © 2024–2026 Raquel Adaia Sandoval Ortega · Python: From Lost to Boss I · https://sandovalortega.com/python-lost-to-boss-1/
# Free to reuse with credit: code under the MIT licence, course text under CC BY 4.0 (see LICENSE.txt).
# This tiny script checks that everything is working:
# your environment, your interpreter and the libraries we will use in the course.
# Run it (the "play" button at the top right of VSC) and look at the terminal.

# Anything after a "#" is a comment and will not be executed by Python.

# Import all libraries at the beginning of the script
import numpy as np  # Operations on numbers, vectors and matrices
import pandas as pd  # Tables of data (DataFrames)
import matplotlib  # Plotting
import seaborn as sns  # Prettier plotting, built on top of matplotlib
import scipy  # Scientific computing and statistics (e.g. t-tests)
import statsmodels  # Statistical models (e.g. ANOVA)
import openpyxl  # Lets pandas read and write Excel files

# If you see an error like "ModuleNotFoundError: No module named 'numpy'", there are two usual reasons:
# 1. VSC is not using the Python interpreter of your environment.
#    Press Ctrl + Shift + P (macOS: Cmd + Shift + P), type "Python: Select Interpreter"
#    and choose the one that contains "env" in its path. Then run the script again.
# 2. The library is not installed in your environment.
#    Activate your environment in the terminal and install it with: pip install name_of_the_library
#    (e.g. pip install seaborn)

# If you can read the message below in the terminal, you are ready for Part 2!
print("Hello, Boss! Everything works.")
print(f"numpy version: {np.__version__}")
print(f"pandas version: {pd.__version__}")
print(f"matplotlib version: {matplotlib.__version__}")
print(f"seaborn version: {sns.__version__}")
print(f"scipy version: {scipy.__version__}")
print(f"statsmodels version: {statsmodels.__version__}")
print(f"openpyxl version: {openpyxl.__version__}")
