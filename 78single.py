#single inheritance		
class Animal:		
       def __init__(self,name,species):		
             self.name=name		
             self.species=species		
       def make(self):		
             print("sound made by the animal")		
		
class Dog(Animal):		
        def __init__(self,name,breed):		
              Animal.__init__(self,name,species="Dog")		
              self.breed=breed		
        def make(self):		
              print("Bark")		
d=Dog("Dog","Doggerman")		
d.make()		
		
a=Animal("Dog","dog")		
a.make()		