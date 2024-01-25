# 2. Numpy
# Using NumPy create random vector of size 20 having only float in the range 1-20. 
# Then reshape the array to 4 by 5
# Then replace the max in each row by 0 (axis=1)
# (you can NOT implement it via for loop)

import numpy as np 

# random.uniform will generate float numbers in the range of 1 to 20
# random.uniform() will generate float numbers from 0 to 1
randomVector = np.random.uniform(1,20, size=20)
print("Random Vector: ")
print(randomVector)

# we are reshaping randomvector to 4 by 5, we are passing as parameter to reshape()
reshapeArray = randomVector.reshape(4,5)
print(" ")
print("Reshape Array: ")
print(reshapeArray)

# np.argmax means we are finding max value in each row and axis=1 means it will operate on row wise (horizontal)
maxValue = np.argmax(reshapeArray,axis=1)
reshapeArray[np.arange(reshapeArray.shape[0]),maxValue] = 0
print(" ")
print("Replace Max in each row by 0: ")
print(reshapeArray)