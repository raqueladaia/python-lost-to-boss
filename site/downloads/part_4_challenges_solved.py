################################################################################
# Welcome to the challenges of Part 4!
################################################################################
# © 2024–2026 Raquel Adaia Sandoval Ortega · Python: From Lost to Boss I · https://sandovalortega.com/python-lost-to-boss-1/
# Free to reuse with credit: code under the MIT licence, course text under CC BY 4.0 (see LICENSE.txt).

# There are 2 TODO actions before the challenges: complete them and set a breakpoint
# at the print() before the challenges begin.
# (The Statistical Analysis at the end of the script has its own TODOs, #1 to #4.)

# First step: import all libraries
import numpy as np
import pandas as pd

# Second step: We will create a DataFrame to work with #########################

# Define the number of rows we want in the DataFrame
n_rows = 50  # TODO: Select an integer above 30

# Define which columns we are going to have
columns = ['animal', 'sex', 'experimental_condition', 'weight']

# Use a list comprehension to generate a list of mouse names
# (you will learn list comprehensions in Part 6; just run it)
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


# It's time to create the DataFrame ############################################
# TODO: Uncomment your preferred method and run the following script

# METHOD #0. Fill the data by column
df = pd.DataFrame()
df['animal'] = mice
df['sex'] = sexes
df['experimental_condition'] = exp_conds
df['weight'] = random_weights

# # METHOD #1. Fill all data all at once
# data_array = np.vstack((mice, np.array(sexes), np.array(exp_conds), random_weights))
# df = pd.DataFrame(columns=columns, data=data_array.T)
# # Notice the use of .T (transpose) - Figure out what it does.
# df['weight'] = df['weight'].astype(float)  # REQUIRED with this method: np.vstack mixed text and numbers in one array, so the weight column is not numeric (dtype object)

# # METHOD #2. Generate first a dictionary and then convert it to a DataFrame
# dict_temp = {'animal': mice,
#              'sex': sexes,
#              'experimental_condition': exp_conds,
#              'weight': random_weights}
# df = pd.DataFrame(dict_temp)

# # METHOD #3. A dictionary comprehension (you will learn list comprehensions in Part 6) to generate a dictionary
# # and then convert it to DataFrame. zip() pairs each column name with its data.
# all_data = [mice, sexes, exp_conds, random_weights]
# dict_temp = {k:v for k, v in zip(columns, all_data)}
# df = pd.DataFrame(dict_temp)
# # You can merge the previous two lines like this:
# # df = pd.DataFrame({k:v for k, v in zip(columns, all_data)})
# # Or all the lines like this:
# # df = pd.DataFrame({k:v for k, v in zip(columns, [mice, sexes, exp_conds, random_weights])})

print()

############################################
# Challenge 1:
# Collect all females
# Separate by experimental condition.
# Collect their weight.
# Average their weight.
# In which experimental condition are females larger?
############################################

# Collect the females
cond_females = df['sex'] == 'F'
df_females = df[cond_females]
# Separate by experimental condition
cond_exp = df_females['experimental_condition'] == 'exp'
cond_ctrl = df_females['experimental_condition'] == 'ctrl'
df_exp = df_females[cond_exp]
df_ctrl = df_females[cond_ctrl]
# Collect their weight
exp_weights = df_exp['weight']
ctrl_weights = df_ctrl['weight']
# Average their weight and round to 2 decimals
avg_exp_weight = np.round(np.mean(exp_weights), 2)
avg_ctrl_weight = np.round(np.mean(ctrl_weights), 2)
# In which experimental condition are females larger?
print(f"Average weight of females: exp = {avg_exp_weight} g, ctrl = {avg_ctrl_weight} g")
print(f"Are females larger in the experimental condition? {avg_exp_weight > avg_ctrl_weight}")

############################################
# Challenge 2:
# Generate a new column “included_in_paper”.
# Fill it with randomly generated True and False values.
# Collect the included mice.
# If you need 20 mice for statistical significance, do you need to include new mice? How many?
############################################

# 1. Generate a new column informing whether the animal is included in the paper or not
# and fill it with randomly generated True and False values.
# ...give the name of the new column
new_col = "included_in_paper"
# ...generate random 0 (=False) and 1 (=True) values where the probability of True is 0.65
prob_included = 0.65
included_animals = np.random.binomial(1, prob_included, n_rows)
# ...transform the 0s and 1s into a boolean
included_bool = included_animals.astype(bool)
# ...add the new column
df[new_col] = included_bool
# 2. Collect the data of the animals included in the paper
df_paper = df[df[new_col]]
# 3. Do I need to include more mice for statistical significance?
min_needed = 20
n_mice_in_paper = df_paper.shape[0]
include_new_decision = min_needed > n_mice_in_paper
# max(0, ...) avoids a negative number when you already have enough mice
n_missing = max(0, min_needed - n_mice_in_paper)
print(f"Mice included in the paper: {n_mice_in_paper}")
print(f"Do I need to include new mice? \n\t\t\t\t{include_new_decision}")
print(f"How many? {n_missing}")

# Additional exploration of the new DataFrame
# ... check the indices in df_paper
indices_df_paper = df_paper.index
print(indices_df_paper)
# THINK! ... Are the indices consecutive? Why? What happened?
# Do I get the same row if I use .iloc or .loc?
idx_to_check = 7
row_iloc = df_paper.iloc[idx_to_check]  # .iloc looks for the POSITION: the 8th row of df_paper
label_of_that_row = df_paper.index[idx_to_check]  # The LABEL (index) of that same row
row_loc = df_paper.loc[label_of_that_row]  # .loc looks for the LABEL: same row as row_iloc
print(f"Position {idx_to_check} of df_paper has the label {label_of_that_row}: mouse {row_iloc['animal']}")
# CAREFUL: df_paper.loc[7] looks for the LABEL 7. If mouse m8 was not included, it raises a KeyError!
# THINK! ... What is the difference between iloc and loc?
# Now, let's reset the index
df_paper = df_paper.reset_index(drop=True)
indices_df_paper_after_reset = df_paper.index
print(indices_df_paper_after_reset)
# THINK! ... What did the reset do? What happens if drop=False?

############################################
# Challenge 3:
# Collect the animals that are included in the paper.
# Separate by sex and experimental condition.
# Print the average weight for each group.
############################################

# 1. Collect the animals included in the paper
# DONE in challenge 2 when I defined df_paper

# 2. Separate the animals by sex and experimental condition
males_bool = df_paper['sex'] == 'M'
control_bool = df_paper['experimental_condition'] == 'ctrl'

# 3. Print the average weight for each group
# ... Collect the weights of each group
males_ctrl = df_paper[males_bool & control_bool]['weight']
males_exp = df_paper[males_bool & ~control_bool]['weight']
females_ctrl = df_paper[~males_bool & control_bool]['weight']
females_exp = df_paper[~males_bool & ~control_bool]['weight']

# ... Average the weights of each group and round to 1 decimal
avg_m_ctrl = np.round(np.mean(males_ctrl), 1)
avg_m_exp = np.round(np.mean(males_exp), 1)
avg_f_ctrl = np.round(np.mean(females_ctrl), 1)
avg_f_exp = np.round(np.mean(females_exp), 1)

# ... Print
print(f"Males:\n\tExperimental: {avg_m_exp}\n\tControl: {avg_m_ctrl}\nFemales:\n\tExperimental: {avg_f_exp}\n\tControl: {avg_f_ctrl}")

############################################
# Statistical Analysis
############################################

# Time to figure out if your treatment has worked!
# We are going to perform a 2-way ANOVA because we have two independent variables
# These independent variables are: sex and experimental_condition
# and we will also assess their interaction
# Our dependent variable is the weight of the mice

# We need to import the libraries that will help us with the ANOVA and the post-hoc tests
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from scipy import stats

# EXPERIMENT: make the groups differ (uncomment ONE option, re-run the whole script and see how the statistics change)
# Our weights are random numbers around 30 g, so without any change the groups should NOT differ.
# lambda x: ... is a tiny one-line function; with axis=1, apply() runs it on each ROW, so x is one mouse
# "a if condition else b" is a one-line if/else (you will learn if/else in Part 6)
# np.random.binomial(1, p, 1)[0] is 1 with probability p, and 0 otherwise (like flipping a coin)

# TODO #1: Uncomment OPTION A, re-run the whole script and investigate the changes in the data.
# Have the statistics changed?
# OPTION A: exp mice gain 16% of their weight (with probability 0.55),
# ctrl mice lose 5% of their weight (with probability 0.45)
df['weight'] = df.apply(lambda x:
                        x['weight'] + x['weight'] * (0.16 * np.random.binomial(1, 0.55, 1)[0])
                        if x['experimental_condition'] == 'exp'
                        else x['weight'] - x['weight'] * (0.05 * np.random.binomial(1, 0.45, 1)[0]),
                        axis=1)  # axis=1: the function is applied to each ROW (each mouse)

# OPTION B: create differences between sexes AND experimental conditions.
# The probability of the weight change is given by this dictionary:
# probs = {'M': 0.9,
#          'F': 0.1,
#          'ctrl': 0.45,
#          'exp': 0.55}
# # First change the weight based on the experimental condition
# df['weight'] = df.apply(lambda x:
#                         x['weight'] + x['weight'] * (0.16 * np.random.binomial(1, probs[x['experimental_condition']], 1)[0])
#                         if x['experimental_condition'] == 'exp'
#                         else x['weight'] - x['weight'] * (0.05 * np.random.binomial(1, probs[x['experimental_condition']], 1)[0]),
#                         axis=1)
# # TODO #2: Proceed changing the weight based on the sex
# # Every mouse gains 10% of its weight, with the probability of its sex
# df['weight'] = df.apply(lambda x:
#                         x['weight'] + x['weight'] * (0.10 * np.random.binomial(1, probs[x['sex']], 1)[0]),
#                         axis=1)
# # TODO #3: Change the probabilities in the dictionary (e.g. 'M': 0.6, 'F': 0.3) and re-run the script
# # a few times. What happens to the statistics?
# # Hint: smaller differences between the groups are often missed: with ~50 mice, the test does not have
# # enough statistical power to detect them every time.

# First, the independent variables have to be categorical
df['sex'] = df['sex'].astype('category')
df['experimental_condition'] = df['experimental_condition'].astype('category')

# Fit the model
# C(variable, Sum) treats the variable as categorical with "Sum" coding, which a Type III ANOVA needs
# to give correct p-values. The "*" means: sex + experimental_condition + their interaction (sex:experimental_condition)
model = ols('weight ~ C(sex, Sum) * C(experimental_condition, Sum)', data=df).fit()

# Perform the ANOVA
# Type III (with Sum coding) tests each effect adjusted for all the others, including the interaction.
# In a balanced design Type II and Type III give the same result; Type II is preferred when there is no interaction.
anova_results = anova_lm(model, typ=3)  # typ=3 specifies Type III sums of squares

print(anova_results.to_string())  # .to_string() prints the whole table (without hiding columns behind "...")

# How to read the table:
# - There is one row per effect: sex, experimental_condition and their interaction (the row with ":")
# - The PR(>F) column contains the p-values: the effect is significant if p < 0.05
# - The Intercept row can be ignored (it only tests if the average weight is different from 0, which we know!)
# - Residual is the variability that the model cannot explain

# Read the p-value of the interaction directly from the table: .loc[row, column]
p_interaction = anova_results.loc['C(sex, Sum):C(experimental_condition, Sum)', 'PR(>F)']
print(f"Interaction p-value: {p_interaction:.2g} -> " + ("look at the follow-up t-tests below" if p_interaction < 0.05 else "not significant: the main effects in the table answer the question; the t-tests below are only an example"))

# Post-hoc tests
# Only look at these tests if the interaction row of the ANOVA has p < 0.05.
# If there is no interaction, the main effect of experimental_condition in the ANOVA already answers the question.
# A significant interaction means that the treatment works differently in males and females.
# Then we ask "has the treatment worked?" in each sex separately: exp vs ctrl within the males,
# and exp vs ctrl within the females (simple effects of the treatment), with t-tests.
# We correct for the 2 tests (Bonferroni: significant if p < 0.05 / 2).
alpha_corrected = 0.05 / 2

# Let's start with the males
males = df.query('sex == "M"')
males_exp_weight = males.query('experimental_condition == "exp"')['weight']
males_ctrl_weight = males.query('experimental_condition == "ctrl"')['weight']

# equal_var=False runs Welch's t-test, which does not assume that both groups have the same variance
t_statistic, p_value = stats.ttest_ind(males_exp_weight, males_ctrl_weight, equal_var=False)
print("Males, exp vs ctrl:")
print(f"t-statistic: {t_statistic:.4f}")
print(f"p-value: {p_value:.2g}")
print(f"Significant after Bonferroni correction? {p_value < alpha_corrected}")

# TODO #4: Do the same for the females
females = df.query('sex == "F"')
females_exp_weight = females.query('experimental_condition == "exp"')['weight']
females_ctrl_weight = females.query('experimental_condition == "ctrl"')['weight']

t_statistic, p_value = stats.ttest_ind(females_exp_weight, females_ctrl_weight, equal_var=False)
print("Females, exp vs ctrl:")
print(f"t-statistic: {t_statistic:.4f}")
print(f"p-value: {p_value:.2g}")
print(f"Significant after Bonferroni correction? {p_value < alpha_corrected}")
