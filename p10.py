class Circle: 
    
    def __init__(self,radius):
        self.radius = radius
        
    
    def area(self):
        area = (22/7) * (self.radius**2)
        print("Area is :",area)
        
        
    def perimeter(self):
        perimeter = 2 * (22/7) * (self.radius**2)
        print("perimeter is:",perimeter)
        
        
c1 = Circle(2.45)

c1.area()
c1.perimeter()