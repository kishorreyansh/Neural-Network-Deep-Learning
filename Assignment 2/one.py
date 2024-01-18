# Write a program that takes two strings from the user: first_name, last_name. Pass these variables to 
# fullname function that should return the (full name).

# o For example:
# ▪ First_name = “your first name”, last_name = “your last name”
# ▪ Full_name = “your full name”

first_name = input("Enter the First String: ")
last_name = input("Enter the Second String: ")

def fullname(first_name,last_name):
    # concatenating the first_name and last_name and storing in fullname
    fullname =  first_name + ' ' + last_name
    return fullname
print("Full Name: ",fullname(first_name,last_name))


# o Write function named “string_alternative” that returns every other char in the full_name string. 
# Str = “Good evening”
# Output: Go vnn

# Note: You need to create a function named “string_alternative” for this program and call it from 
# main function.

def string_alternative(fullname):
    fullNameValue = fullname(first_name,last_name)

    # First Approach through for loop  
    finalFullName = ''
    for i in range(len(fullNameValue)):
        if(i % 2 == 0):
            finalFullName += fullNameValue[i]
    print("Full Name with every other Character: ",finalFullName) 

    # Second Approach through step
    # finalFullName = fullNameValue[::2]
    # print("Full Name Alternate Characters: ",finalFullName)      

def main():
    string_alternative(fullname)

if __name__ == "__main__":
    main()