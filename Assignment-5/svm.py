# 2. Implement linear SVM method using scikit library
# Use the same dataset above
# Use train_test_split to create training and testing part
# Evaluate the model on test part using score and 
# classification_report(y_true, y_pred)

import pandas as pd

# pip install -U scikit-learn
from sklearn.model_selection import train_test_split
# Importing a Naive Bayes library
from sklearn.svm import SVC
# Importing a Metrics library to Use classification_report and accuracy_score functions
from sklearn.metrics import classification_report, accuracy_score

# Importing the datasets from glass.csv
glass_dataframe = pd.read_csv('glass.csv')

# Dropping Type Column and assigning other columns to variable X
X = glass_dataframe.drop("Type",axis=1)
Y = glass_dataframe[['Type']]

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X,Y,test_size=1/4, random_state = 0)

# Creating an instance of a model i.e., SVC
svmdata = SVC()

# Training the Model
svmdata.fit(X_Train,Y_Train)

# Predicting the Test set result 
Y_Pred = svmdata.predict(X_Test)

# Generate the classification report
classificationreport = classification_report(Y_Test, Y_Pred)
print("Classification Report: ")
print(classificationreport)

# Calculate the accuracy
accuracy = accuracy_score(Y_Test, Y_Pred)
print("Support Vector Machine Accuracy is: {:.2f}%".format(accuracy * 100))
print(" ")