import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os as os

import pandas as pd
states_finance = pd.read_csv("STATES.csv")
test_results = pd.read_csv("NEAP.CSV")

merge_left = pd.merge(states_finance, test_results, on = ["STATE", "YEAR"], how = "right")
print(merge_left.head(3))

merge_left.drop(merge_left[merge_left["YEAR"]==2017].index, inplace = True)
print(merge_left.head(20))

## Create list of columns that show breakdown of Revenue and Expenditure
column_list_drop = ['FEDERAL_REVENUE', 'STATE_REVENUE', 'LOCAL_REVENUE', 'INSTRUCTION_EXPENDITURE', 'SUPPORT_SERVICES_EXPENDITURE', 'OTHER_EXPENDITURE', 'CAPITAL_OUTLAY_EXPENDITURE']
print(column_list_drop)

## Drop list of columns that show breakdown of Revenue and Expenditure
column_list_drop = merge_left.drop(column_list_drop, axis = 1)
merge_left = column_list_drop
print(merge_left.head())

merge_left = merge_left.sort_values(["YEAR", "AVG_SCORE"], ascending = [False, False])
print(merge_left.head())

merge_left = merge_left.groupby('YEAR').head(5).reset_index(drop=True)
print(merge_left.head(25))

## Plot on line graph
fig, ax = plt.subplots()
x = ['Vermont', 'NewJersey', 'Minnesota', 'NewHampshire', 'Massachusetts']
y = [290, 292, 293, 294, 297]
plt.plot(x, y, marker = "v", color = "g")
ax.set_xlabel("State")
ax.set_ylabel("Test Result")
ax.set_title("US State Math Results 2015")
plt.show()
