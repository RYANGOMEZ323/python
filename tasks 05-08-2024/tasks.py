####1)convert a str to dict and length as its value
##def str_to_dict(string):
##    return {string:len(string)}
##user = input("enter a string : ")
##print(str_to_dict(user))
####2)find the len of str without using len function
##def str_length(string):
##    i = 0
##    for j in string:
##        i+=1
##    return i
##user = input("enter a string : ")
##print(str_length(user))
##3)max repeated character in the str
user = input("enter a string : ")
max_chr = {}
for i in user:
    if i  in max_chr:
        max_chr[i]+=1
    else:
        max_chr[i]=1
print(max_chr)    

print(max_chr.items().sort())
##4)remove white space from the str
user = input("enter a string : ")
remove = user.replace(" ","")
print(remove)
##5)reverse the string without using slicing method
user = input("enter a string : ")
user = list(user)
user.reverse()
user = "".join(user)
print(user)
##1. define a function to convert temperature to fahrenheit
def temperature_to_fahrenheit(a):
    f = (a*9/5)+32
    return f
user = int(input("enter the temperature:"))
print(temperature_to_fahrenheit(user),"*F")
##2. define a calculator function (e.g format, def calculator(a, b, operation( +/-/*,etc )))
def calculator(a,b,operation):
    if operation == "+":
        return a+b
    elif operation == "-":
        return a-b
    elif operation == "*":
        return a*b
    else:
        return "invalid operation , pls use only (+ ,-,*)"
print(calculator(2,5,"+"))
##3. create a function for rolling a dice, when we call the function,it should randomly generate a number between 1 and 6
import random
dice = [1,2,3,4,5,6]
rolling_dice = random.choice(dice)
print(rolling_dice)
##4. find the area of the circle (use math module) define function!
import math
from math import *
def area_of_circle(radius):
    return pi*(radius**2)
user = int(input("enter the radius(in cm):"))
print("THE AREA OF THE CIRCLE IS ",area_of_circle(user),"sq.cm")
