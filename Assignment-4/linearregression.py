# 2. Linear Regression
    # a) Import the given “Salary_Data.csv”
    # b) Split the data in train_test partitions, such that 1/3 of the data is reserved as test subset.
    # c) Train and predict the model.
    # d) Calculate the mean_squared error
    # e) Visualize both train and test data using scatter plot

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# pip install -U scikit-learn
from sklearn.model_selection import train_test_split
# Importing a library
from sklearn.linear_model import LinearRegression

# Mean Squared Error using scikit-learn
from sklearn.metrics import mean_squared_error

# Importing the datasets from data.csv
df_dataframe = pd.read_csv('Salary_Data.csv')

X = df_dataframe[['YearsExperience']]
Y = df_dataframe[['Salary']]

print(" ")
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X,Y,test_size=1/3, random_state = 0)

# Fitting Simple Linear Regression to the training set
# Creating an instance of a model i.e., LinearRegression
regressor = LinearRegression()

# Training the Model
regressor.fit(X_Train,Y_Train)

# Predicting the Test set result ￼
Y_Pred = regressor.predict(X_Test)

# Calculate the mean_squared error or Mean Squared Deviation
mse = mean_squared_error(Y_Test,Y_Pred)
print("MEAN SQUARED ERROR: ",mse)

# Visualize both train and test data using scatter plot
plt.scatter(X_Train, Y_Train, label="Training Data")
plt.scatter(X_Test, Y_Test, label="Test Data")
plt.plot(X_Test, Y_Pred, label="Linear Regression")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.title("Linear Regression: Salary vs Years of Experience")
plt.show()

