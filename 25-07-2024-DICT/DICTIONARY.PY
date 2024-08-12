##DICTIONARY-{key:value}
#ordered
#changeable
#does not allow duplicate
##Tasks:
##1. create a dictionary and add 2 new items to it.
##2. Remove two key:value pairs from the dictionary
##3. check whether a key exists in the dictionay
##4. check whether a value exists in the dictionary
##5. update the key and value using if-else
##6. merge two dictionaries and store it in a variable 
##7. create a dictionary and print its values using loop
##8. create a nested dictionary and print its values using nested loop
##9. add new key,value pair to the nested dictionary



####Tasks:
####1. create a dictionary and add 2 new items to it.
##bike = {"brand":"royal enfield","model":"classic 350"}
##bike.update({"color":"red"})
##bike.update({"year":2024})
##print(bike)
##print("----------------------------------------------------------------------------")
##print()
##
####2. Remove two key:value pairs from the dictionary
##bike = {'brand': 'royal enfield', 'model': 'classic 350', 'color': 'red', 'year': 2024}
##bike.pop("year")
##bike.pop("color")
##print(bike)
##print("----------------------------------------------------------------------------")
##print()
##
####3. check whether a key exists in the dictionay
##bike = {'brand': 'royal enfield', 'model': 'classic 350', 'color': 'red', 'year': 2024}
##key = input("enter a key :")
##if key in bike.keys():
##    print(key,"exists in ",bike)
##else:
##    print(key,"does not exists in ",bike.keys())
##
##print("----------------------------------------------------------------------------")
##print()
##
##
####4. check whether a value exists in the dictionary
##bike = {'brand': 'royal enfield', 'model': 'classic 350', 'color': 'red', 'year': 2024}
##value = input("enter a value :")
##if value in bike.values():
##    print(value,"exists in ",bike)
##else:
##    print(value,"does not exists in ",bike.values())
##print("----------------------------------------------------------------------------")
##print()
##
##
####5. update the key and value using if-else
##bike = {'brand': 'royal enfield', 'model': 'classic 350', 'color': 'red', 'year': 2024}
##key = "color"
##if key in bike:
##    bike.update({"color":"black"})
##    print(bike)
##else:
##    bike.update({"color":"black"})
##    print(bike)
##print("----------------------------------------------------------------------------")
##print()
##
####6. merge two dictionaries and store it in a variable 
##a = {'brand': 'royal enfield', 'model': 'classic 350'}
##b = {'color': 'red', 'year': 2024}
##c = {}
##c.update(a)
##c.update(b)
##
##print(c)
##print("----------------------------------------------------------------------------")
##print()
##
####7. create a dictionary and print its values using loop
##bike = {'brand': 'royal enfield', 'model': 'classic 350', 'color': 'red', 'year': 2024}
##for value in bike.values():
##    print(value)
##print("----------------------------------------------------------------------------")
##print()

##8. create a nested dictionary and print its values using nested loop
bikes = {"bike_1":{'brand': 'royal enfield', 'model': 'classic 350'},"bike_2":{"brand": "yamaha", "model":"fascino z"},"bike_3":{"brand":"honda","model":"unicorn"}}
##bike_1:{'brand': 'royal enfield', 'model': 'classic 350'}
##bike_2:{"brand": "yamaha", "model":"fascino z"}
##bike_3:{"brand":"honda","model":"unicorn"}
##bikes = {"bike_1":bike_1,"bike_2":bike_2,"bike_3":bike_3}
for x , y in bikes.items():
    print(bikes[x])
    for key in y:
        print(key,":",y[key])
print("----------------------------------------------------------------------------")    
print()

##9. add new key,value pair to the nested dictionary
bikes = {"bike_1":{'brand': 'royal enfield', 'model': 'classic 350'},"bike_2":{"brand": "yamaha", "model":"fascino z"},"bike_3":{"brand":"honda","model":"unicorn"}}
bikes["bike_1"].update({"color":"red"})
bikes["bike_2"].update({"color":"blue"})
bikes["bike_3"].update({"color":"black"})
print(bikes)






