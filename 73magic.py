class Employee:
    name="Harry"
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    
e=Employee()
print(e.name)
print(len (e))



from magic import Employee
e=Employee("Harry")
print(str(e))
print(len(e))
print(repr(e))
e()
