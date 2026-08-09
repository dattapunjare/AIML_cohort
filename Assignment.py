''' Name:  Datta Punjare
    Batch: August
    Day:   1
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