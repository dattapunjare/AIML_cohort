'''Name: Datta Punjare
   Day 5: Lecture
   Date : 13 aug
   Topics : 1. Type Hints , 2. Classes  , 3. object , 4.  Attribute , 5) methods , 7)special methods,
   '''


#Type hint : After execution code it tells what Datatype of output you get
def add(a:int,b:int):
  return a+b

# Type Hints , class and methods
def add(a,b):
  return a + b
add(5.5,2)

name : str = 'Datta'
age : int = 20
height : float = 5.4
is_student : bool = True

print(name)
print(age)
print(height)
print(is_student)

#Takes any type of data even mention int it can take float values

#Syntax:
#variable_name : type = value

def square(number: int) -> int:    # -> Only tells data type or datatype of output
    return number * number         #int

def get_name() -> str:             #string
    return 'Zophie'

print(square(5))
print(get_name())

# multiple type hint

def print_id(user_id: int | str):  # | to seprate
    print(user_id)

print_id(100)
print_id("A100")

  #user id parameter is for two diff data types

#typehint : collection

numbers: list[int] = [10, 20, 30]
student_marks: dict[str, int] = {'Alice': 90}
point: tuple[int, int] = (10, 20)

print(numbers)
print(student_marks)
print(point)

def double(number: int) -> int:
    return number * 2

print(double('Hi'))

#Never throw error and never check in runtype and never throw error type hind is just for reading and just documentation and for user

def calculate_average(marks: list[int]) -> float:
    return sum(marks) / len(marks)

def display_student(name: str, marks: list[int]) -> None:
    average: float = calculate_average(marks)
    print(f'Student: {name}')
    print(f'Average: {average:.2f}')

display_student('Datta', [75, 40, 62])

#creting a class
#class : is a blueprint to creting object
#object : things build from classes

'''Syntax: Class C_name:
  body
  obj = class'''

class Student:

  student1 = student()
  student2 = student()

#Attributes : Belong to specific obj

student = Student()
student.name='Datta'
student.age = 20
student.marks(33,56,76)
print(student.name)



print(student.name)
print(student.age)
print(student.marks)

#__init__ () : To create automaatic object , no need to create objectc again

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student('Datta', 20)


print("Student Name:", student.name)
print("Student Age:", student.age)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}.")
        print(f"My age is {self.age}.")

student = Student('Datta', 20)
student.introduce()

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print('Insufficient balance.')

    def show_balance(self):
        print(f'Balance: {self.balance}')

account = BankAccount('Sakshi', 5000)
account.deposit(1500)
account.withdraw(2000)
account.show_balance()

#str : return string

class student:
  def __init__(self,name):
    self.name =name
  def __str__(self):
      return f'{self.name}'
student = student("Datta")
print(student)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

student = Student("Datta", 20)
print(student)

#__repr__ : to return string

def __repr__(self):
    return f'Student({self.name!r})'
    print(repr(student))

stud = student('Datta')
print(stud)
print(repr('Datta'))

#__len__ : Special method that returns the length of variable

def __len__(self):
  return len(self.songs)
  len(playlist)

