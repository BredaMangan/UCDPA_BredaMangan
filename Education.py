import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt
import os as os

import pandas as pd
states_finance = pd.read_csv("STATES.csv")
## check how many rows and columns are in my data
print(states_finance.shape)

## Check the head of the data
print(states_finance.head(5))

##Check the tail of the data
print(states_finance.tail(5))

## check for missing values
print(states_finance.isnull().sum())

## Check the names of the columns
print(states_finance.columns)

## Check for the Primary Key(unique values and = to total no. of rows)
print(len(states_finance.STATE.unique()))

## Check how many unique states
print(len(states_finance.STATE.unique()))

## Check if the number of states by the number of years match the total number of rows.
print(51*25)

##Check the data type of the data
print(states_finance.dtypes)

##Check unique year values
print(states_finance.YEAR.unique())

##Check how many times each year appeared
print(states_finance['YEAR'].value_counts())

## Drop the null values - year 1992
droprows = states_finance.dropna()
print(states_finance.shape, droprows.shape)

## Check shape of data after dropping rows
states_finance = droprows
print(states_finance.shape)

## Check for duplicates
drop_duplicates = states_finance.drop_duplicates()
print(states_finance.shape, drop_duplicates.shape)

##Sort Year, Expenditure and Revenue in descending order
states_finance = states_finance.sort_values(["YEAR", "TOTAL_REVENUE", "TOTAL_EXPENDITURE"], ascending = [False, False, False])
print(states_finance.head())

## Check if revenue and expenditure breakdown add up to total revenue and total expenditure
revenue = int(7709079 + 50904567 + 30603616)
expenditure = int(42587272 + 26058021 + 3995951 + 6786142)
total_revenue = 89217262
total_expenditure = 85320133

## Check if the expenditure is equal to the total expenditure
if total_expenditure == expenditure:
    print("total expenditure is equal to expenditure")
elif total_expenditure < expenditure:
    print("total expenditure is less than expenditure")
else:print("total expenditure is greater than ependiture")

##check if the revenue is equal to the total revenue
if total_revenue == revenue:
    print("total revenue is equal to total revenue")
elif total_revenue < revenue:
    print("total revenue is less than revenue")
else:print("total revenue is greater than revenue")

## Create a list of the Columns with revenue and expenditure.
column_list = ['TOTAL_REVENUE', 'FEDERAL_REVENUE', 'STATE_REVENUE', 'LOCAL_REVENUE', 'TOTAL_EXPENDITURE', 'INSTRUCTION_EXPENDITURE', 'SUPPORT_SERVICES_EXPENDITURE', 'OTHER_EXPENDITURE', 'CAPITAL_OUTLAY_EXPENDITURE']
print(column_list)

## Divide the columns in the column_list by 1000000
states_finance[column_list] = states_finance[column_list].div(100000).round(2)
print(states_finance.shape)

## Create list of columns that show breakdown of Revenue and Expenditure
column_list_drop = ['FEDERAL_REVENUE', 'STATE_REVENUE', 'LOCAL_REVENUE', 'INSTRUCTION_EXPENDITURE', 'SUPPORT_SERVICES_EXPENDITURE', 'OTHER_EXPENDITURE', 'CAPITAL_OUTLAY_EXPENDITURE']
print(column_list_drop)

## Drop list of columns that show breakdown of Revenue and Expenditure
column_list_drop = states_finance.drop(column_list_drop, axis = 1)
states_finance = column_list_drop
print(states_finance)

## Create a list of the States using an array
array = np.array(['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
       'Colorado', 'Connecticut', 'Delaware', 'District of Columbia',
       'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana',
       'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
       'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
       'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
       'New Jersey', 'New Mexico', 'New York', 'North Carolina',
       'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
       'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee',
       'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
       'West Virginia', 'Wisconsin', 'Wyoming'])
print(array)




