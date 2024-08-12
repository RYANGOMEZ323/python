####CONTROL STATEMENTS
###1)BREAK
###2)CONTINUE
###3)PASS
##
###1)i)BREAK STATEMENT IN FOR LOOP:
##print("BREAK STATEMENT IN FOR LOOP:")
##for i in range(11):
##    if i == 6:
##        break
##    else:
##        print(i)
##print("--------------------------------")
###ii)BREAK STATEMENT IN WHILE LOOP:
##print("BREAK STATEMENT IN WHILE LOOP:")
##i = 0
##while i <= 11:
##    if i  == 6:
##        print(i)
##        i+=1
##        break
##    else:
##        print(i)
##        i+=1
##        
##print("--------------------------------")
##
###2)i)CONTINUE STATEMENT IN FOR LOOP:
##print("CONTINUE STATEMENT IN FOR LOOP:")
##for i in range(11):
##    if i == 6:
##        continue
##    else:
##        print(i)
##print("--------------------------------")
##
###ii)CONTINUE STATEMENT IN WHILE LOOP:
##print("CONTINUE STATEMENT IN WHILE LOOP:")
##i = 0
##while i <= 11:
##    if i  == 6:
##        print(i)
##        i+=1
##        continue
##    else:
##        print(i)
##        i+=1
##        




l = [-5, 2, 0, 7, -3, 0, 4]

##Hint: Assign separate variable to store results.
##
##1. Count the number of positive, negative, and zero values in a list
##2. Sum all the positive numbers from the above list.
##
##3. Print all even numbers under 20 using while loop (3 different cods using normal while, using continue, using pass)
##4. count the total number of vowels from a string.
##
##5. check whether the given number is a prime number
##	Prime number means: a number being divided only by 1 and itself. eg: 1,3,5,7
##
##6. find the maximum value from the list using loop
##7. Print Fibonacci series up to 50.
##	fibonacci series eg: 0,1,1,2,3,5,8,13,21,34



##----------------------------------------------------------------------



###1. Count the number of positive, negative, and zero values in a list
##
##
##l = [-5, 2, 0, 7, -3, 0, 4]
##positive = 0
##negative = 0
##zero = 0
##for i in l:
##    if i > 0 :
##        positive+=1
##    elif i<0:
##        negative+=1
##    else :
##        zero+=1
##print("positive numbers",positive)
##print("negative numbers",negative)
##print("zero numbers",zero)
##
####2. Sum all the positive numbers from the above list.    
##
##l = [-5, 2, 0, 7, -3, 0, 4]
##s = 0
##for i in l :
##    if i > 0:
##        s+=i
##print(s)
##
##
##
##
##3. Print all even numbers under 20 using while loop (3 different cods using normal while, using continue, using pass)
##
##using  normal while
##i = 0
##while i < 20:
##    i+=2
##    print("EVEN NUMBER",i)
##print("---------------------------------------------------------------------")
##using continue
##i = 0
##while i < 20:
##    if i % 2 != 0 :
##        i+=1
##        print("even numbers",i)
##        continue
##    else:
##        i+=1
##print("---------------------------------------------------------------------")
##using pass
##i = 0
##while i < 20:
##    if i % 2 != 0 :
##        i+=1
##        print("Even Numbers",i)
##        pass
##    else:
##        i+=1
##print("----------------------------------------------------------------------")
##4. count the total number of vowels from a string.
##
##a = input("enter a word:")
##count = 0
##for i in a:
##    if i in ("aeiouAEIOU"):
##        count+=1
##print("the total no of vowels from" ,a,"is",count)
##print("-----------------------------------------------------------------------")
####5. check whether the given number is a prime number
####	Prime number means: a number being divided only by 1 and itself. eg: 1,3,5,7
##a = int(input("enter  a number :"))
##for i in range(1,a):
##    if a % i == 0:
##        print(a,"is not a prime number")
##        break
##else:
##    print(a,"is a prime number")
print("-------------------------------------------------------------------------")
##6. find the maximum value from the list using loop
l = [-5, 2, 0, 7, -3, 0, 4]
for i in l:
    if i>l:
        print("max")























        


