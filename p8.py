class Student:
    
    name = "M Haris Tariq"
    
    # Class Method
    def changename(cls,name):
        cls.name=name
        
s1 = Student()

print(s1.name)

s1.changename("Harry Potter")

print(s1.name)


        
