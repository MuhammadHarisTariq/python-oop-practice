class Car:
    
    def __init__(self,type):
        self.type = type
    
    @staticmethod
    def start():
        print("My Car is Starting")
        
    @staticmethod
    def stop():
        print("My car is stoping")
        
class Toyota(Car):
    
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
        
        
t1 = Toyota("fortuner","electric")

print(t1.name)
print(t1.type)
t1.start()
t1.stop()

        

        
    