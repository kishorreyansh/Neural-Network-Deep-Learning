# Use the if statement conditions to write a program to print the letter grade based on an input class score. 
# Use the grading scheme we are using in this class.

marks = int(input("Enter your marks (0-100) : "))

def grade(marks):
    if marks >= 90 and marks <= 100:
        return "A"
    elif marks >= 80 and marks <= 89:
        return "B"
    elif marks >= 70 and marks <= 79:
        return "C"
    elif marks >= 60 and marks <= 69:
        return "D"
    else:
        return "F"
    
print("Grade: ",grade(marks))
