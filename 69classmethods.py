class Employee:
    company = "apple"
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")
    @classmethod   
    def changecompany(cls,newCompany):
        cls.company=newCompany
e1=Employee()
e1.name="Harry"
e1.show()
e1.changecompany("tesla")
e1.show()
print(Employee.company)