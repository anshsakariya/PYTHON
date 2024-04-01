class Employees:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])
e=Employees("Harry",12000)
print(e.name)
print(e.salary)


string="john-15000"
e1=Employees(string.split("-")[0],string.split("-")[1])
e1 = Employees.fromstr(string)
print(e1.name)
print(e1.salary)
