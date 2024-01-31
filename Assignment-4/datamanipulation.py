# 1. Data Manipulation
    # a. Read the provided CSV file ‘data.csv’.
    # b. https://drive.google.com/drive/folders/1h8C3mLsso-R-sIOLsvoYwPLzy2fJ4IOF?usp=sharing
    # c. Show the basic statistical description about the data.
    # d. Check if the data has null values.
    # i. Replace the null values with the mean
    # e. Select at least two columns and aggregate the data using: min, max, count, mean.
    # f. Filter the dataframe to select the rows with calories values between 500 and 1000.
    # g. Filter the dataframe to select the rows with calories values > 500 and pulse < 100.
    # h. Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”.
    # i. Delete the “Maxpulse” column from the main df dataframe
    # j. Convert the datatype of Calories column to int datatype.
    # k. Using pandas create a scatter plot for the two columns (Duration and Calories). 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd  # pip install pandas

# Importing the datasets from data.csv
df_dataframe = pd.read_csv('data.csv')

# Show the basic statistical description about the data.
statistical_description = df_dataframe.describe()
print("*********** STATISTICAL DESCRIPTION ***********")
print(statistical_description)
print(" ")

# Applying Only on variables with NaN values
# Check if the data has null values. Replace the null values with the mean
for i in df_dataframe.columns[df_dataframe.isnull().any(axis=0)]:     
    df_dataframe[i].fillna(df_dataframe[i].mean(),inplace=True)
print(df_dataframe)
print(" ")

# Select at least two columns and aggregate the data using: min, max, count, mean
selected_colums = ['Duration', 'Pulse']
aggregrated_data = df_dataframe[selected_colums].agg(['min', 'max','count','mean'])
print(" ****** AGGREGRATED DATA ********** ")
print(aggregrated_data)

# Filter the dataframe to select the rows with calories values between 500 and 1000
filtered_df1 = df_dataframe[(df_dataframe['Calories'] >= 500) & (df_dataframe['Calories'] <= 1000)]

# Filter the dataframe to select the rows with calories values > 500 and pulse < 100
filtered_df2 = df_dataframe[(df_dataframe['Calories'] > 500) & (df_dataframe['Pulse'] < 100)]

# Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”.
df_modified = df_dataframe.drop(columns='Maxpulse')

# Delete the “Maxpulse” column from the main df dataframe
df_dataframe.drop(columns='Maxpulse',inplace=True)

# Convert the datatype of Calories column to int datatype.
df_dataframe['Calories'] = df_dataframe['Calories'].astype(int)
print(" DATAFRAME Calories Column INT")
print(df_dataframe.info())
print(" ******* DATA MODIFIED DATA FRAME ******* ")
print(df_modified)

# Using pandas create a scatter plot for the two columns (Duration and Calories)
plt.scatter(df_dataframe['Duration'], df_dataframe['Calories'])
plt.xlabel('Duration')
plt.ylabel('Calories')
plt.title('DURATION AND CALORIES GRAPH')
plt.show()