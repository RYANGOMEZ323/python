##EXCEPTIONAL HENDLING:


#The try block lets you test a block of code for errors.

#The except block lets you handle the error.

#The else block lets you execute code when there is no error.

#The finally block lets you execute code, regardless of the result of the try- and except blocks.


#TYPES OF ERROR:
#1)ZeroDivisionError
#2)ValueError
#3)KeyError
#4)NameError
#5)IndexError
#6)TypeError

##try-except

try:
    print(a)
except:
    print("ERROR FOUND")
else:
    print("ERROR NOT FOUND")
finally:
    print("The 'try except' is finished")

#ZeroDivisionError:
try:
    print(25/0)
except:
    print("a number cannot be divided by zero")

#ValueError:
try:
    print(int("hello"))
except:
    print("invalid literal for int() with base 10: 'hello'")

#KeyError:
try:
    d = {'a': 1}
    print(d['b'])
except:
    print("key 'b' is not found")
    
    
#NameError:
try:
    print(a)
except:
    print("variable a is not found")
    
#IndexError:
a = [1,2,3,4,5,6]
try:
    print(a[7])
except:
    print("list out of range")


#TypeError:
try:
    print("a" + 3)
except:
    print("str cannot be concatenate with int")

##NESTED TRY-EXCEPT:
try:
    a = int(input("ENTER A NUMBER : "))
    try:
        print(a/0)
    except:
        print("ZeroDivisionError:a number cannot be divided by zero")
except:
    print("invalid number")

##RAISE EXCEPTIONAL ERROR:
a = int(input("ENTER A NUMBER: " ))
if a<0:
    raise Exception(a,"IS LESS THAN 0 ")
else:
    print(a)
        
