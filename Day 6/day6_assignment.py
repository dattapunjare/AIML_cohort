
#Assignment

def even_numbers():
    for number in range(2,10,2):
        yield number


for num in even_numbers():
    print(num)

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

# Decorator using decorator syntax

def decorator(function):

    def wrapper():
        print("Hello ! which movie you like to watch :")
        function()
    return wrapper

@decorator
def movie():
    text = input("Enter name of movie you like to watch : ")
    print(f"Wow {text} nice choice!")

# Call the function
movie()

#context manager

# With context manager
with open("data.txt") as file:
    content = file.read()

# Without context manager (manual)
file = open("data.txt")
content = file.read()
file.close()

#__enter__ and __exit__
class MyContext:
    def __enter__(self):
        print('Entering')
        return self

    def __exit__(self, exc_type, exc_value, tb):
        print('Leaving')

# Using the context manager
with MyContext():
    print('Inside')
