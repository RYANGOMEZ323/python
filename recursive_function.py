# print("hello world")

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# print(tri_recursion(6))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))  # Output: 120

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(5))  # Output: 5
# 1. Factorial Calculation
# Problem: Compute the factorial of a number n (denoted as n!).

# Recursive Solution:

# python
# Copy co
# de
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))  # Output: 120
# 
# def power(x, n):
#     if n == 0:
#         return 1
#     else:
#         return x * power(x, n - 1)

# print(power(2, 3))
# recurse function
# def power(n,x):
#     if x == 0:
#         return 1
#     else :
#         return n * power(n,x-1)
# print(power(5,2))
# def sum_list(lst):
# ##    if not lst:
# ##        return 0
# ##    else:
#        return lst[0] + sum_list(lst[1:])

# def reverse_string(s):
#    if len(s) == 0:
#        return s
#    else:
#        return reverse_string(s[1:]) + s[0]

# print(reverse_string("hello"))  
# print("hrllo")

def fibonacci(n):
   if n <= 1:
       return n
   else:
       return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))  # Output: 
def str_length(string)
    i = 0
    for j in string:
        i+=1
    return i
user = input("enter a string : ")
print(str_length(user))
