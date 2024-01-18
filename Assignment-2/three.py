# Write a program, which reads heights (inches.) of customers into a list and convert these 
# heights to centimeters in a separate list using:
# 1) Nested Interactive loop.
# 2) List comprehensions

# Nested Interactive loop.
# num_customers = int(input("Enter the Total Number of Customers: "))
# # creating empty list for height in inches
# heights_inches = []
# # creating empty list for height in inches
# heights_cm = []

# This function converts inches to centimeters of a customers
# def inches_to_cm(height_in_inches):
#     return height_in_inches * 2.54

# for i in range(num_customers):
#     height = float(input(f"Enter Height (in inches) for Customer {i + 1}: "))
#     heights_inches.append(height)
#     heights_cm.append(inches_to_cm(height))

# Printing the height of the customers in centimeters
# print("Heights in centimeters:", heights_cm)

# List comprehensions
def inches_to_cm(height_in_inches):
    return height_in_inches * 2.54

num_customers = int(input("Enter the Total Number of Customers: "))
heights_inches = [float(input(f"Enter height (in inches) for customer {i + 1}: ")) for i in range(num_customers)]
heights_cm = [inches_to_cm(height) for height in heights_inches]

# Printing the height of the customers in centimeters
print("Heights in centimeters:", heights_cm)