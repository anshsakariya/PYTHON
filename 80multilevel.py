#multilevel inheritance
class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    
    def show(self):
        print(f"Name:{self.name}")
        print(f"species:{self.species}")
    

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed=breed
    
    def show(self):
        Animal.show(self)
        print(f"Breed:{self.breed}")

class gold(Dog):
    def __init__(self,name,color):
        Dog.__init__(self,name,breed="gold")
        self.color=color
    
    def show(self):
        Dog.show(self)
        print(f"color:{self.color}")

a=Dog("tommy","Black")
a.show()
print(gold.mro())
