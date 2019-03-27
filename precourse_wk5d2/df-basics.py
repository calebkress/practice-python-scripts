# Part 1 - The Basics of Data Frames
import pandas as pd

df = pd.read_csv('./data/winequality-red.csv', delimiter=';')
# How many rows and columns are in the DataFrame?
df.shape
# What data type is in each column?
# Are all of the variables continuous, or are any categorical?
# How many non-null values are in each column?
df.info()
# What are the min, mean, max, median for all numeric columns?
df.describe()
