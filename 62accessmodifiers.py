class Employee:
    #constructor is defined
    def __init__(self):
        self.name="Harry"
a=Employee()
print(a.name)
print(a.__dir__())


print("==================")
class student:
    def __init__(self):
        self.name="Harry"
    def _funName(self):  #protected method
         return "codewithharry"

class subject(student): #inherited class
    pass

obj=student()
obj1=subject()
print(dir(obj))

#calling by objects of students pass
print(obj.name)
print(obj._funName())
#calling by objects of subjects class
print(obj1.name)
print(obj1._funName())
