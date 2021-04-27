import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os as os

import pandas as pd
states_finance = pd.read_csv("STATES.csv")
test_results = pd.read_csv("NEAP.CSV")

## Merge STATES & NEAP
merge_test_results = pd.merge(states_finance, test_results, on = ["STATE", "YEAR"], how = "right")
print(merge_test_results.head(3))

## Drop year 2017
merge_test_results.drop(merge_test_results[merge_test_results["YEAR"]==2017].index, inplace = True)
print(merge_test_results.head(20))

## Create list of columns that show breakdown of Revenue and Expenditure
column_list_drop = ['FEDERAL_REVENUE', 'STATE_REVENUE', 'LOCAL_REVENUE', 'INSTRUCTION_EXPENDITURE', 'SUPPORT_SERVICES_EXPENDITURE', 'OTHER_EXPENDITURE', 'CAPITAL_OUTLAY_EXPENDITURE']
print(column_list_drop)

## Drop list of columns that show breakdown of Revenue and Expenditure
column_list_drop = merge_test_results.drop(column_list_drop, axis = 1)
merge_test_results = column_list_drop
print(merge_test_results.head())

## Sort test results in descending order
merge_test_results = merge_test_results.sort_values(["YEAR", "AVG_SCORE"], ascending = [False, False])
print(merge_test_results.head())

## Group by top 5 in each year
merge_test_results = merge_test_results.groupby('YEAR').head(5).reset_index(drop=True)
print(merge_test_results.head(25))

## Plot on line graph - STATES WITH HIGHEST SCORES IN 2015
fig, ax = plt.subplots()
x = ['Vermont', 'NewJersey', 'Minnesota', 'NewHampshire', 'Massachusetts']
y = [290, 292, 293, 294, 297]
plt.plot(x, y, marker = "v", color = "g")
ax.set_xlabel("State")
ax.set_ylabel("Test Result")
ax.set_title("US State Math Results 2015")
plt.show()

## Sorting test results in descending order
test_results = test_results.sort_values(["YEAR", "AVG_SCORE"], ascending = [False, False])
print(test_results.head())