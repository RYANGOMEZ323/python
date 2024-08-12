###COLLECTION MODULE:-
##Counter:-
#A Counter is a sub-class of the dictionary.
#unordered dictionary
import collections
a = ["apple","banana","apple","apple","banana","banana","banana","apple","strawberry"]
b = collections.Counter(a)
print(b)
dic = {"apple":4,"banana":4,"strawberry":1}
c = collections.Counter(dic)
print(c)
##OrderedDict:-
#An OrderedDict is also a sub-class of dictionary but unlike dictionary, it remembers the order in which the keys were inserted.
#While deleting and re-inserting the same key will push the key to the last to maintain the order of insertion of the key.

import collections
ord_dict = collections.OrderedDict()
ord_dict["name = "] = "ryan gomez"
ord_dict["age = "] = 18
ord_dict["DOB = "] = "07-06-2007"
ord_dict["nationality = "] = "Indian"
for a,b in ord_dict.items():
    print(a,b)
#after delting and reinserting
ord_dict["name = "] = "ryan gomez"
ord_dict["age = "] = 18
ord_dict["DOB = "] = "07-06-2007"
ord_dict["nationality = "] = "Indian"

ord_dict.pop("age = ")

ord_dict["age = "]=18

for a,b in ord_dict.items():
    print(a,b)
    
#While deleting and re-inserting the same key will push the key to the last to maintain the order of insertion of the key.
##DefaultDict:-
#A DefaultDict is also a sub-class to dictionary. It is used to provide some default values for the key that does not exist and never raises a KeyError.
#DefaultDict objects can be initialized using DefaultDict() method by passing the data type as an argument.
import collections
def_dict = collections.defaultdict(int) 
   
a = [1,2,3,4,5,5,5,6,2,3,4,8,9,1] 
for i in a:
    def_dict[i] += 1
print(def_dict)

##ChainMap:-
#A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries.
import collections

dict_1 = {1: 1, 2: 2}
dict_2 = {3: 3, 4: 4}
dict_3 = {5: 5, 6: 6}
c = collections.ChainMap(dict_1,dict_2,dict_3)   
print(c)
##NamedTuple:-
#A NamedTuple returns a tuple object with names for each position which the ordinary tuples lack
import collections
person = collections.namedtuple('person',['name','age','DOB']) 
a = person('ryan',18,'07-06-2007') 
print (a[1])   
print (a.name)
#1. _make(): This function is used to return a namedtuple() from the iterable passed as argument.
l = ["ryan",18,"07-06-2007"]
print (person._make(l))
#2. _asdict(): This function returns the OrdereDict() as constructed from the mapped values of namedtuple().
d = { 'name' : "ryan", 'age' : 18 , 'DOB' : '07-06-2007' }
print (a._asdict())

##Deque
#Deque (Doubly Ended Queue) is the optimized list for quicker append and pop operations from both sides of the container.
import collections
from collections import deque 
a = deque(["name","age","DOB"])
print(a)
#Elements in deque can be inserted from both ends. To insert the elements from right append() method is used and to insert the elements from the left appendleft() method is used.
a = deque([2,4,6])
a.appendright(8)
print(a)
a.appendleft(0)
print(a)
#Elements can also be removed from the deque from both the ends. To remove elements from right use pop() method and to remove elements from the left use popleft() method.
a = deque([2,4,6])
a.popright()
print(a)
a.popleft()
print(a)













