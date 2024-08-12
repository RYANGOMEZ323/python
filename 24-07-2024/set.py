##SET
#unorderd
#unindexed
#does not allow duplicate
#unchangeable
#syntax - {}

####JOIN :-
####UNION( | ) :-
##set1 = {1,2,3,4,5,6,7,8,9}
##set2 = {2,4,6,8,10}
##set3 = set1.union(set2)
##set3 = set1 | set2
##print(set3)
####INTERSECTION( & ) :-
##set1 = {1,2,3,4,5,6,7,8,9}
##set2 = {2,4,6,8,10}
##set3 = set1.intersection(set2)
##set3 = set1 & set2
##print(set3)
####DIFFERENCE( - ) :-
##set1 = {1,2,3,4,5,6,7,8,9}
##set2 = {2,4,6,8,10}
##set3 = set1.difference(set2)
##set3 = set1-set2
##print(set3)
####SYMMETRIC DIFFERNCE( ^ ) :-
##set1 = {1,2,3,4,5,6,7,8,9}
##set2 = {2,4,6,8,10}
##set3 = set1.symmetric_difference(set2)
##set3 = set1^set2
##print(set3)


##TASKS:-
##SET Tasks:
##1. create a set - add 2 items and remove 2 items 
##2. print the union, intersection, difference, symmetric difference of two sets using operators
##3. check whether an item is present in the set or not using if else
##4. loop and print the elements of the set
##5. print the square of the items in the set.
##6. check whether the set is superset or subset
##7. convert a string to set


##SET Tasks:

##1. create a set - add 2 items and remove 2 items 
a = {1,2,3,4,5,6,7,8,9}
a.update({10,11})
print("10 and 11 are added ",a)
a.remove(2)
a.remove(3)
print("2 and 3 are removed",a)
print("----------------------------------------------------------------")

##2. print the union, intersection, difference, symmetric difference of two sets using operators
set1 = {1,2,3,4,5,6,7,8,9}
set2 = {2,4,6,8,10,12,14}
print("UNION:",set1 | set2)
print("INTERSECTION:",set1 & set2)
print("DIFFERENCE:",set1 - set2 )
print("SYMMETERIC DIFFERENCE:",set1 ^ set2)
print("----------------------------------------------------------------")

##3. check whether an item is present in the set or not using if else
a = {"LION","TIGER","ELEPHANT","CHEETAH","FOX"}
b = input("ENTER A NAME OF A ANIMAL:")
if b in a :
    print(b," IS PRESENT IN",a)
else:
    print(b,"IS NOT PRESENT IN",a)
print("----------------------------------------------------------------")


##4. loop and print the elements of the set
a = {2,3,4,5,6,7,8,9}
for i in a:
    print(i)
print("----------------------------------------------------------------")

##5. print the square of the items in the set.
a = {2,3,4,5,6,7,8,9}
for i in a :
    print("SQUARE OF ",i,"IS",i**2)
print("----------------------------------------------------------------")

##6. check whether the set is superset or subset
set1 = {1,2,3,4,5,6,7,8,9}
set2 = {1,3,5,7,9}
if set1.issuperset(set2) or set1.issubset(set2):
    print("set1 is a superset of set2")
else:
    print("set1 is not a subset of set2")
if set2.issubset(set1)or set2.issuperset(set1): 
    print("set2 is a subset of set1")
else:
    print("set2 is not a subset of set1")



print("----------------------------------------------------------------")

##7. convert a string to set
a = "animal"
a = set(a)
print(a)
print("----------------------------------------------------------------")

