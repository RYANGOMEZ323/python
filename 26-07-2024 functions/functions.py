00000000000##FUNCTIONS(user-defined)
##keyword - def
##l = []
##def iseven(*numbers):
##    for i in numbers:
##        if i % 2 == 0:
##            l.append(i)
##    return l       
##iseven(1,2,3,4,5,6,7,8)
##print(l)


##Tasks using def:-
##1. define a function to find whether a number is even or odd
##2. define a function to find whether a string is palindrome or not (return True or False)
##3. define a function with (* args) arbitrary arguments condition(*)
##4. define a function with (* * kwargs) arbitrary keyword arguments()
##5. define a function to find the sum of the list
##6. define a function to find the second largest number
##7. define a function to find whether a number is prime or not


##Tasks using def:-
##1. define a function to find whether a number is even or odd
def is_even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
a = int(input('enter a number :'))
print(is_even_or_odd(a))
print("-----------------------------------------")
print()

##2. define a function to find whether a string is palindrome or not (return True or False)

def ispalindrome(word):
    if (word[::-1]==word):
        return "yes it is palindrome"
    else:
        return "no it is not palindrome"
a = input("enetr a word :")
print(ispalindrome(a))
print("-----------------------------------------")
print()

##3. define a function with (* args) arbitrary arguments condition(*)
def add(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total
print(add(34,24,100))
print("-----------------------------------------")
print()

##4. define a function with (* * kwargs) arbitrary keyword arguments()
def person(**name):
    print("his first name is" + name["first_name"])
person(first_name="ryan",last_name="gomez")
print("-----------------------------------------")
print()

##5. define a function to find the sum of the list

def sum_list(l):
    total = 0
    for i in l:
        total += i
    return total
print(sum_list([1,2,3,4]))
print("-----------------------------------------")
print()

##6. define a function to find the second largest number
def sec_largest_no(l):
    l.sort()
    return("second largest no is",l[-2])
print(sec_largest_no([100,10,43,54,68,79]))
print("-----------------------------------------")
print()

##7. define a function to find whether a number is prime or not
def isprime(i):
    if i%2== 0 or i%3==0 or i%5==0 or i%7==0:
        print("no it is not prime")
    else:
        print("yes it is prime")
a = int(input("enter a positive number :"))
isprime(a)
print("-----------------------------------------")
print()
##1. Factorial Calculation
##Problem: Compute the factorial of a number n (denoted as n!).
##
##Recursive Solution:
##
##python
##Copy code
##def factorial(n):
##    if n == 0:
##        return 1
##    else:
##        return n * factorial(n - 1)
##
##print(factorial(5))  # Output: 120
##2. Fibonacci Sequence
##Problem: Find the n-th number in the Fibonacci sequence.
##
##Recursive Solution:
##
##python
##Copy code
##def fibonacci(n):
##    if n <= 1:
##        return n
##    else:
##        return fibonacci(n - 1) + fibonacci(n - 2)
##
##print(fibonacci(5))  # Output: 5
##3. Power of a Number
##Problem: Compute x raised to the power of n (x^n).
##
##Recursive Solution:
##
##python
##Copy code
##def power(x, n):
##    if n == 0:
##        return 1
##    else:
##        return x * power(x, n - 1)
##
##print(power(2, 3))  # Output: 8
##4. Sum of Elements in a List
##Problem: Calculate the sum of all elements in a list.
##
##Recursive Solution:
##
##python
##Copy code
##def sum_list(lst):
##    if not lst:
##        return 0
##    else:
##        return lst[0] + sum_list(lst[1:])
##
##print(sum_list([1, 2, 3, 4, 5]))  # Output: 15
##5. Reverse a String
##Problem: Reverse a string.
##
##Recursive Solution:
##
##python
##Copy code
##def reverse_string(s):
##    if len(s) == 0:
##        return s
##    else:
##        return reverse_string(s[1:]) + s[0]
##
##print(reverse_string("hello"))  # Output: "olleh"


##recursive function:
##power
def power(n,x):
    if x == 0:
        return 1
    else :
        return n * power(n,x-1)
print(power(5,2))


##sum of list
def suml(n):





    




