###MULTIPLICATION TABLE(1 to 5)
##i = 1
##while i<=5 :
##    print(f"MULTIPLICATION TABLE FOR {i} :")
##    for j in range(1,11):
##        print(f"{i} x {j} = {i*j}")
##    print()
##    i+=1
##SECURITY
##CorrectUsername = input("ENTER USER :")
##CorrectPassword = input("ENTER PASSWORD :")
##attempts = 0
##MaxAttempts = 2
##
##while attempts < MaxAttempts:
##    Username = input("ENTER U R USERNAME :")
##    Password = input("ENTER U R PASSWORD :")
##    if(CorrectUsername == Username and CorrectPassword == Password):
##        print("LOGIN SUCCESSFULLY")
##        break
##    else:
##        print("INCORRECT USERNAME OR PASSWORD , PLS TRY AGAIN")
##        attempts += 1
##else :
##    print("MAX NO OF ATTEMPTS REACHED , ACCESS DENIED")





###1) sum of numbers from 1 to 100 :
##i = 1
##s = 0
##while i <= 100:
##    i+=1
##    s+=i
##print(s)
##
##print("__________________________________________________")
##
##
###2) print all even numbers within range of 100 using while loop :
##i = 2
##while i <= 100:
##    print(i)
##    i+=2
##print("____________________________________________________")    
##
##
###3) find a factorial of a number:
##a = int(input("ENTER A POSITIVE NUMBER :"))
##factorial = 1
##for i in range(1,a+1):
##    factorial = factorial * i
##print(factorial,"is the factorial of" ,a)
##
##print("_____________________________________________________")
###4) Assign username and password to variables :
##CorrectUsername = input("enter u r username :")
##CorrectPassword = input("enter u r password :")
##Attempts = 0
##MaxAttempts = 3
##
##while Attempts <= MaxAttempts:
##    Username = input("enter username :")
##    Password = input("enter password :")
##    if(CorrectUsername == Username and CorrectPassword == Password ):
##        print("login successfully ")
##        break
##    else:
##        print("incorrect username or password , try again!")
##        Attempts += 1
##else:
##    print("max no of attempts reached , access denied!")
##
##print("_____________________________________________________")


#1)multiplication tables upto 5th table using for loop:
for i in range(1,6):
    print(f"multiplication table of {i} : ")
    for j in range (1,11):
        print(f"{i} x {j} = {i*j}")
    print("__________________________________________")



#2)multiplication tables upto 5th table using for while:
i = 1
while i <= 5 :
    print(f"multiplication table of {i} : ")
    j = 1
    while j <=10:
        print(f"{i} x {j} = {i*j}")
        j+=1
    i+=1
    print("___________________________________________")
#3)  *
#    **
#    ***
#    ****
#    *****

for i in range(1,6):
    print("* "* i)
print("___________________________________________")

#4)   1
#     1 2
#     1 2 3
#     1 2 3 4 
#     1 2 3 4 5


for i in range (1,6):
    for j in range(1,i+1):
        print(j," ",end = "")
    print()
print("___________________________________________")
#5)  a
#    a b
#    a b c
#    a b c d
#    a b c d e 


for i in range(97 , 102):
    for j in range(97,i+1):
        print(chr(j)," ",end="")
    print()
print("___________________________________________")
#6)  1  2  3   4   5
#    2  4  6   8   10
#    3  6  9   12  15
#    4  8  12  16  20
#    5  10 15  20  25


for i in range(1,6):
    for j in range(1,6):
        print(i*j," ",end="")
    print()
print("___________________________________________")
















    

