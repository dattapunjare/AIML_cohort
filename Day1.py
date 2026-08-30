''' Name:   Datta Punjare
    Cohort: TEP cohort 2026
    Day:    1
    Date:   9 Aug

    Description:
    This file contains the assignment given on day 1.
    It includes example of data type conversion, for loop, and while loop.

    What I have done in day 1:

    - Learned Python basics
    - Learned why Python is used
    - Learned about virtual environments
    - Learned VS Code shortcuts
    - Learned Google Colab
    - Learned Kaggle
    - Learned data types
    - Learned dictionaries
    - Learned slicing
    - Learned if-else
    - Learned loops

'''


 
#  Q1. use for loop 
# Ask the user how many number they want add

n = int(input("How many number you want to add :"))

total = 0

for i in range(n):
    num = int(input("Enter number :"))
    total += num

print("the total sum is :",total)


#Q2. use while loop function
# Program to check password is corrct or not by using while loop

password = ""

while password != "admin":
    password = input("Enter password: ")

print("Correct password")


#Q3. Data type conversion (string to number)

# String input
num_str = "25"

# Convert string to integer
num_int = int(num_str)
print("String to int:", num_int)
