class parentClass:
    def parent_method(self):
        print("this is the parent methods1")
class ChildClass(parentClass):
    def parent_method(self):
        print("Harry")
        super().parent_method()
    def child_methods(self):
        print("this is the child methods2.")
        super().parent_method()
child_object = ChildClass()
child_object.child_methods()
child_object.parent_method()


print("+++++++++++")
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class Programmer:
    def __init__(self,name,id,lang):
        self.name=name
        self.id=id
        self.lang=lang

rohan=Employee("Rohan Das","420")
harry=Programmer("harry","2345","python")
print(rohan.name)
print(harry.id)


print("+++++++++++")
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang

rohan=Employee("Rohan Das","420")
harry=Programmer("harry","2345","python")
print(harry.name)
print(harry.id)
print(harry.lang)
