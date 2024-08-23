#CLASS

class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"Animal(Name: {self.name}, Breed: {self.breed})"  
    
    def bark(self):
        print (self.name,"is barking")
    
    def sleep(self):
        print(self.name,"is sleeping")
        
dog_1 = Animal("Candy","Labarador")
dog_2 = Animal("Max","German Shepard")
# print(dog_1)
# print(dog_2)
# dog_1.bark()   
# dog_2.bark() 
# dog_1.sleep()   
# dog_2.sleep() 