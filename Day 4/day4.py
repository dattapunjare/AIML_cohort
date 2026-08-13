''' Name : Datta Punjare 
    Day 4: 12 Aug
    Batch: AIML


def hello():
  print('Hey')
  print('Hey')
  print('Hey')
hello()
hello()
print('one morre time')
hello()

def add(a,b):   #define function
  return a+b

n1 = int(input("Enter first value :"))    #take input from user
n2 = int(input("Enter first value :"))


print(add(n1,n2))   #call function


#parameter:value given in the function
#Argument:Actual value that we pass to the function



def division(a, b):
    #normal
    normal_div = a / b
    #int division

    floor_div = a // b
    #modulas
    modulus = a % b
    return normal_div , floor_div ,modulus
n1 = int(input("Enter first value :"))
n2 = int(input("Enter secound value :"))

print(division(n1,n2))

import random
def get_answer(n):
  if n==1:
    return'it is certain'
  elif n==2:
    return 'Ask again later'

r = random.randint(1,9)
print(get_answer(r))

spam = None
print(spam)

#value absent use none

eggs = 'global'
def spam():
  eggs='local'  #same name
  print(eggs)#rule of access global v
spam()
print(eggs)

42/0

#exception handling:use to manage runtime errors

def spam(divided_by):
  try:
    return 42/divided_by
  except ZeroDivisionError:
    print('Error:invalid argument')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(3))

#this is animation program
import time, sys
indent = 0 # How many spaces to indent
indent_increasing = True # Whether the indentation is increasing or not
try:
    while True: # The main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10th of a second.
        if indent_increasing:
            # Increase the number of spaces:
            indent = indent + 1
    if indent == 20:
        # Change direction:
        indent_increasing = False
    else:
        # Decrease the number of spaces:
        indent = indent - 1
    if indent == 0:
        # Change direction:
        indent_increasing = True
except KeyboardInterrupt:
    sys.exit()
