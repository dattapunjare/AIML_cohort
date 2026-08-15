
''' Day 6:
   Date : 14 aug
   Name: Datta Punjare
   Description : Topics that are covered on day 5
   Topics : 1)Iterators ,2) Generators ,3) Decorators ,4)  Content manager 7)special methods,
'''


for number in [10,20,30]:  #Iterable: get the set of item one by one until it gets empty
    print(number)         #things ir do is iterable

numbers = [10, 20, 30]
iterator = iter(numbers)
next(iterator)
next(iterator)

numbers = [10, 20, 30]
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))  #Stop iteration:stops when there is no elements

class Countdown:
    def __init__(self, start):
        self.current = start    ## self.current stores the starting number

    def __iter__(self):        ## __iter__() makes the object an iterator
        return self

    def __next__(self):  #take one by one item
        if self.current < 0:        # Check if countdown has below 0
            raise StopIteration
        number = self.current #store self
        self.current -= 1  #
        return number



for number in Countdown(3):
    print(number)

def get_numbers():
  yield 10      # yield is used to return a value from the generator
  yield 20
  yield 30

  next(get_numbers())
  next(get_numbers())
  next(get_numbers()) #Failuare: to get diffrent value why? because this is generator and it will go with fresh start with every call

#next(get_numbers())

#next(get_numbers())

def get_num():
  yield 10
  yield 20
  yield 30

number=get_num()
print[next(get_num)] # actually getting new value from generator
print[next(get_num)]
print[next(get_num)]

def count_up_to(limit):
    number = 1
    while number <= limit:  #Gives value to the the yield
        yield number
        number += 1

for number in count_up_to(5):
    print(number)

numbers = list(
    range(1,1_000_001))

def count_up_to(limit):
    number = 1
    while number <= limit:
        yield number
        number += 1

# Using the generator
for number in count_up_to(5):
    print(number)

squares_list = [n*n for n in range(5)]
print(squares_list)

# Generator
squares_gen = (n*n for n in range(5))
for val in squares_gen:
    print(val)

[n*n for n in range(5)]
#print all things

(n*n for n in range(5))# added generator by swapping []

squares = (n*n for n in range(5))

print(next(squares)) #0
print(next(squares))#1
print(next(squares))
print(next(squares))
print(next(squares))

def even_numbers(limit):
    for number in range(2, limit + 1, 2):
        yield number


for number in even_numbers(10):
    print(number)

#Assignment

def even_numbers():
    for number in range(2,10,2):
        yield number


for num in even_numbers():
    print(num)

def decorator(function):
  def wrapper():
    print("bol na bhidu")
    function
  return wrapper()

def say_hello():
  user_name=str(input("enter your name :")) #take one value
  print(f"hey {user_name}")#gives another val
function=say_hello()

say_hello()#you can call a function

#Decorator:function that takes another function as an argument

#wrapper : replace original funtion


def say_hello():
  user_name = str(input("your name? :"))
  print(f"hello, {user_name}")


def decorator(func):
  def wrapper():
    print("bol na bhidu")
    func()

  return wrapper()

say = decorator(say_hello)
say()

# handling any arguments
def decorator(func):
  def wrapper(*args, **kwargs):
    result =func(*args, **kwargs)
    return result
  return wrapper

@decorator
def add(a,b):
  return a + b

add(10,20)

#self study context manager