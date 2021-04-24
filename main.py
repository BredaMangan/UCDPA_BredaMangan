import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os as os



## User defined function

a = 853.20
b = 892.17

def sum_numbers(num1 = a, num2 = b):
    total = num1 + num2
    return total
summation = sum_numbers()
print(summation)
def sum_percent1(num3 = a, num4 = summation):
    total = num3 / num4
    return total
percent1 = sum_percent1
print(sum_percent1())
def sum_percent2(num5 = b, num4 = summation):
    total = num5 / num4
    return total
percent2 = sum_percent2
print(sum_percent2())
def check_sum(num6 = sum_percent1, num7 = sum_percent2):
    total = num6 + num7
    return total
checkans = check_sum
print(check_sum)







#892.17
#782.48
#723.89
#688.68


