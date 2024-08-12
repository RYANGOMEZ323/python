##TUPLE
#ordered
#unchangeable
#allow duplicates
##1. create a tuple and add a new item to it
##2. create a tuple and remove an existing item
##3. unpack a tuple and assign to 2 variables i.e, a & b
##4. count the occurences of an item in a tuple
##5. concatenate two tuples
##6. remove all duplicates from the tuple using loop
##7. insert a list into the tuple and append an item to the list inside the tuple!
##8. create a set and add and remove an item in the set
##9. create a nested tuple and print the items of the nested tuple

##TUPLE TASKS
##1. create a tuple and add a new item to it
T = ("LION","TIGER","ELEPHANT")
T = list(T)
T.append("CHEETAH")
T = tuple(T)
print(T)
print("----------------------------------------")
##2. create a tuple and remove an existing item
t = ("LION","TIGER","ELEPHANT")
t = list(t)
t.remove("TIGER")
print(t)
print("----------------------------------------")
##3. unpack a tuple and assign to 2 variables i.e, a & b
t = ("LION","TIGER","ELEPHANT")
(a,*b)=t
print("t =",t)
print("a =",a)
print("b =",b)
print("----------------------------------------")
##4. count the occurences of an item in a tuple
a = ("LION","TIGER","ELEPHANT","LION","LION","ELEPHANT")
b = a.count("LION")
c = a.count("TIGER")
d = a.count("ELEPHANT")
print("NO OF LION IN THE TUPLE IS ",b)
print("NO OF TIGER IN THE TUPLE IS ",c)
print("NO OF ELEPHANT IN THE TUPLE IS ",d)
print("----------------------------------------")
##5. concatenate two tuples
a = (12,34,56,123)
b = (1,2,3,4)
c=a+b
print(c)
print("----------------------------------------")
##6. remove all duplicates from the tuple using loop
a = ("LION","TIGER","ELEPHANT","LION","LION","ELEPHANT")
b = []
for i in a :
    if i not in b:
        b.append(i)
b = tuple(b)
print(b)
print("----------------------------------------")

##7. insert a list into the tuple and append an item to the list inside the tuple!
a = ([1,2,3,4,5,6,7],)
b = a[0]
b.append(8)
print(a)
print("----------------------------------------")





##8. create a set and add and remove an item in the set
a = {"LION","TIGER","ELEPHANT","CHEETAH","FOX"}
a.add("BEAR")
print(a)
a.discard("TIGER")
print(a)
print("----------------------------------------")


##9. create a nested tuple and print the items of the nested tuple
a = ((1,2),(3,4,5,6),7,8)
for i in a :
    print(i)







