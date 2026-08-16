
''' Day 7:
   Date : 16 aug
   Name: Datta Punjare
   Description : Topics that are covered on day 7
   Topics : Python Libraries, Numpy, Array Operations, urllib, requests, get and post, Array vs list 
'''

#numpy

import math
math.sqrt(25)

def square_root(num):
  sqrt = num ** 0.5
  return sqrt
  print(square_root(25))

#libraries are use for this :
# math & calculation 2.Files 3.website and internet 4.graphs and charts 5.dates and time 6. data processing 7. databases 8.ML models

"""1.math & calculation 2.Files 3.website and internet 4.graphs and charts 5.dates and time 6. data processing 7. databases 8.ML models"""

#Numpy : include number,numerical operations, array
#math->indivisual element

#python list
import numpy as np
numbers = [10,20,30] #numpy array

#Numpyarray
import numpy as np
num=np.array([10,20,30])   #A list is not organise where array is in organised manner
print(num)

#with a list :

number=[10,20,30]
result=[]
for n in numbers:
  result.append(n*2)
print(result)

#with an array :

import numpy as np
number=np.array([10,20,30])
result=num*2
print(result)

#3 quick way to create arraay

import numpy as np
np.zeros(5)

np.ones(5)

np.arange(0,10,2)

print(np.ones(5))

print(np.zeros(5))

print(np.arange(0,10,2))

#accessing and changing element

import numpy as np
numbers=np.array([10,20,30])
numbers[0]

print(number)

numbers[1]=99

print(numbers)

import numpy as np

numbers=np.array([10,20,30])
numbers+5


numbers*2

numbers /10

print(numbers)
print(numbers*2)
print(numbers/10)

#working with two arrays

import numpy as np
a=np.array([10,20,30])
b=np.array([1,2,3])


print(a*b)
print(a+b)

#useful numpy function

numbers=np.array([10,20,30,40,50])
print(np.sum(numbers))


np.mean(numbers)

np.max(numbers)

print()

#shapes : rows and columns

import numpy as np
numbers=np.array([
    [1,2,3],
    [4,5,6]])
numbers.shape

numbers[0,1]

print(numbers.shape)
print(numbers[0,1])

#read webpage

import urllib.request
response=urllib.request.urlopen('https://google.com')
response.status

#urllib

#pip install third party a 3rd party library

pip install requests

import requests as rq
rq.get("https://google.com")

#making a get request and reading it back
import requests as rq
response=requests.get('')
response.status



#get - askfor data, post- send data

#Assignment

#array operation
import numpy as np
marks = np.array([67,88,66,82,87])
print("Marks:", marks)
print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Highest:", np.max)

# Requests and JSON

# making get request , and reading it back

res = requests.get('https://www.google.com/')
res.status_code

res.text

res.raise_for_status()
 # raises an error automatically on 404,500,etc

# Getting JSON data - python objects , not text

res = requests.get('https://www.google.com/')
data = res.json()
data['name']

#get vs post - asking vs sending

#get
requests.get(url)

#post
requests.post(url, json = data)
