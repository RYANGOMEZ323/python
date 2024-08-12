####LOCAL VARIABLE AND GLOBAL VARIABLE
##x = "apple" #- global variable-can be called both inside and outside 
##def fruits():
##    global y
##    y = "banana" #- local variable - can be only called while inside , can be called outside whien using a keyword "global"
##    print(y)
##fruits()
##print(x)
##print(y)
##
####LAMDA
###syntax = lambda arguments : expression
##division = lambda x,y : x/y
##print(division(4,2))
##add = lambda *x : sum(x)
##print(add(2,5,7,9,1,4,4,44,5,7))


###local variable and global variable
##1. assign a variable inside the function and print outside the function
##2. modify a global variable using a function
##
###lambda function
##1. create a lambda function to multiply two arguments
##2. create a lambda function to add two arguments
##3. create a lambda function to subtract two arguments
##
### lambda + map function
##
##1. find the squares of the elements inside the list
##2. subtract 1 from all the elements inside the list
##3. find the len of the strings present inside the list



####tasks
####local variable and global variable
####1. assign a variable inside the function and print outside the function
##
##def fruits():
##    y = "banana"
##    print(y)
##fruits()   
##print("________________________________________")
##print()
####2. modify a global variable using a function
##def fruits():
##    global x 
##    x = "apple"
##fruits()
##print(x)
##print("________________________________________")
##print()
##
#####lambda function
####1. create a lambda function to multiply two arguments
##
##multiplication = lambda x,y : x*y
##print(multiplication(45,10))
##print("________________________________________")
##print()
##
####2. create a lambda function to add two arguments
##add = lambda x,y: x+y
##print(add(45,10))
##print("________________________________________")
##print()
##
####3. create a lambda function to subtract two arguments
##
##subtract = lambda x,y:x-y
##print(subtract(45,10))
##print("________________________________________")
##print()
##
##### lambda + map function
##
####1. find the squares of the elements inside the list
##
##l = [2,4,6,8,10]
##def sq(x):
##    return x**2
##print(list(map(sq,l)))
##print("________________________________________")
##print()
##
####2. subtract 1 from all the elements inside the list
##
##def sub(x):
##    return x-1
##print(list(map(sub,l)))
##print("________________________________________")
##print()
##
####3. find the len of the strings present inside the list
##
##l = ["apple","banana","orange","strawberry"]
##print(list(map(len,l)))
##print("________________________________________")
##print()
## Tasks
##1. define a function and iterable(i.e, a list ), use them in map
##2. define a function and iterable, use that and filter items
##3. define a function for reduce from functools module, and use them to find the largest value
##4. create a module and import and use them in another file
##5. import math module and run sqrt, ceil, floor and pi with proper explanation in comment line
##
##1. define a function and iterable(i.e, a list ), use them in map
def add(x):
    return x+1
l = [2,4,6,7,8,1,9]
print(list(map(add,l)))
print("________________________________________")
print()
##2. define a function and iterable, use that and filter items
def isEven(x):
    return x%2==0
    
l = [2,4,6,7,8,1,9]
print(list(filter(isEven,l)))
print("________________________________________")
print()
##3. define a function for reduce from functools module, and use them to find the largest value
import functools
from functools import reduce
print(reduce(lambda x,y : x if x > y else y,l))
print("________________________________________")
print()
##4. create a module and import and use them in another file
import practice
practice.name("RYAN")
print("________________________________________")
print()
##5. import math module and run sqrt, ceil, floor and pi with proper explanation in comment line
import math
from math import *
print(int(sqrt(64)))
print(ceil(78.34))
print(floor(45.99))
print(pi)
print("________________________________________")
print()






