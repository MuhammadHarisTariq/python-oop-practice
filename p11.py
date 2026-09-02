class Employee:
    
    def __init__(self,role,depart,salary):
        self.role = role
        self.depart = depart
        self.salary = salary
        
    
    def ShowDetails(self):
        print("Role:",self.role)
        print("Depart:",self.depart)
        print("Salary:",self.salary)
        


class Engineer(Employee):
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Mechanical Engineer","Engineering","5000")
        
    def ShowDetails1(self):
        print(self.name)
        print(self.age)
        
e1 = Employee("Accountant","Finance",60000)
e1.ShowDetails()

E2 = Engineer("Haris",22)

E2.ShowDetails1()
E2.ShowDetails()
        
    