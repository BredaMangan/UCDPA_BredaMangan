import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt
import os as os

import pandas as pd
states_finance = pd.read_csv("STATES.csv")
## check how many rows and columns are in my data
print(states_finance.shape)

## check for missing values
print(states_finance.isnull().sum())
