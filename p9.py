class Complex:
    
    def __init__(self,real,img):
        self.real = real
        self.img = img 
        
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
        
    def __sub__(self,other):
        
        Real = self.real - other.real
        Img = self.img - other.img
        
        return Complex(Real,Img)
        
    
num1 = Complex(3,5)
num1.showNumber()

num2 = Complex(7,6)
num2.showNumber()

num3 = num1 - num2

num3.showNumber()
        
        