####STRING
##a = "I am a student"
##b = "My name is william "
##c = [1,2,3,4,5,6,7,]
###INDEXING
##print(a[7])#-s
###REVERSE INDEXING
##print(a[-5])#-u
###SLICING
##print(a[0:6])#-I am a
##print(a[5:])#-a student
###NEGATIVE INDEXING
##print(c[-6:])#-[2, 3, 4, 5, 6, 7]
###LENGTH
##print(len(a))#-14
##print(len(b))#-19
####print(len(c))#-7
##
##
#1) a
#   b c
#   d e f
#   g h i j
n = 5
num = 97
for i in range(0,n):
    for j in range(0,i+1):
        ch= chr(num)
        print(ch,end="")
        num = num+1
    print()


#2)PALINDROME
a = input("(PALINDROME)enter a word:")
b = a[::-1]
if (a==b):
    print("yes it is palindrome" )
else:
    print("no it is not palindrome")


#3)ANAGRAM
a= input("(ANAGRAM)enter a word:")
b= input("enter a word:")
if (sorted(a)==sorted(b)):
    print("Yes,it is anagram")
else:
    print("No, its is not angram")


#4)PRINT THE VOWELS FROM THE STRING
a = input("(VOWELS)enter a word:")
for i in a:
    if i in("aeiouAEIOU") :
##    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        print(i)
#5)CHECK TWO WORDS ARE SAME??
a = input("enter a word:")
b = input("enter a word:")
if ((a.upper())==(b.upper())):
    print ("yes,the two words are same")
else:
    print("no,the two words are not same")












    
