#multiple inheritance

class Employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"the name is {self.name}")

class Dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"the dance is {self.dance}")

class DanceEmployee( Employee,Dancer):
    def __init__(self,dance,name):
        self.dance=dance
        self.name=name

a=DanceEmployee("raj","shivani")
print(a.name)
print(a.dance)
a.show()
print(DanceEmployee.mro())
