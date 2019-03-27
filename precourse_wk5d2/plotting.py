import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

df = pd.read_csv('./data/winequality-red.csv', delimiter=';')

# 1. Plot the average amount of `chlorides` for each `quality` value (1 from Part 3).
df.plot(kind='scatter', x='quality', y='chlorides')

# 2. Plot the `alcohol` values against `pH` values. Does there appear to be any relationship between the two?
df.plot(kind='hist', x='alcohol', y='pH')

# 3. Plot `total_acidity` values against `pH` values. Does there appear to be any relationship between the two?
df.plot(kind='scatter', x='total_acidity', y='pH')

# 4. Plot a histogram of the `quality` values. Are they evenly distributed within the data set?
df['quality'].plot(kind='hist')

# 5. Plot a boxplot to look at the distribution of `citric acid`.
df['citric acid'].plot(kind='box')
