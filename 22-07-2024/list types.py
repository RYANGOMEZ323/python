###List Tasks:
##
##1. create a list with random interger values and store it in a variable
##now, find and print the even numbers and odd numbers from the list.
##
##2. create two lists 'a' and 'b' and add its elements and show the result.
##   i.e, a =[1,2], b = [2,2]
##        result = [3,4]
##
##3. find the squared value of the items inside the list 
##
##4. Create a list from a string where each character is a list element (e.g., "hello" becomes ['h', 'e', 'l', 'l', 'o']).
##
##5. Flatten a nested list (e.g., [[1, 2, 3], [4, 5], [6, 7, 8]] becomes [1, 2, 3, 4, 5, 6, 7, 8]).
##
##6. Remove all duplicates from a list while maintaining order.
##
##7. Find the common elements between two lists.


###List Tasks:

##1. create a list with random interger values and store it in a variable
##now, find and print the even numbers and odd numbers from the list.
l = [1,2,3,4,5,6,7,8,9,]
for i in l:
    if i%2==0:
        print(i,"is a even number")
    else:
        print(i,"is a odd number")
print("--------------------------")

##2. create two lists 'a' and 'b' and add its elements and show the result.
##   i.e, a =[1,2], b = [2,2]
##        result = [3,4]
a = [1,3,5,7]
b = [2,4,6,8]
c = []
for i in range(4):
     c.append(a[i]+b[i])
print(c)
print("--------------------------")

##3. find the squared value of the items inside the list
l = [1,2,3,4,5,6,7]
SQ = []
for i in l:
     SQ.append(i**2)
     print("square value of ",i,"is",i*i)
print(SQ)
print("--------------------------")
##4. Create a list from a string where each character is a list element (e.g., "hello" becomes ['h', 'e', 'l', 'l', 'o']).
a = input("ENTER A STRING :")
b=list(a)
print(b)

print("--------------------------")

##5. Flatten a nested list (e.g., [[1, 2, 3], [4, 5], [6, 7, 8]] becomes [1, 2, 3, 4, 5, 6, 7, 8]).
l = [[1, 2, 3], [4, 5], [6, 7, 8]]
f = []
for i in l:
    f.extend(i)
print(f)
print("--------------------------")

##6. Remove all duplicates from a list while maintaining order.
l = ["pen","pencil","eraser","pen","sharpener","eraser"]
res = []
for i in l:
     if i not in res:
          res.append(i)
print(res)


##print("--------------------------")
##7. Find the common elements between two lists.
a = [2,6,7,8,3]
b = [1,2,3,6,7]
c = []
for i in a:
     if i in b:
          c.append(i)
print("THE COMMOM ELEMENTS ARE",c)



    



