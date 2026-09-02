class Result:
    
    def __init__(self,phy,math,chem):
        self.phy = phy
        self.math = math
        self.chem = chem
        # self.percentage =((self.phy+self.math+self.chem)/300) * 100
        
    
    # def calpercentage(self):
    #     return ((self.phy+self.math+self.chem)/300) * 100
    @property
    def calpercentage(self):
        return ((self.phy+self.math+self.chem)/300) * 100
    
        
       

r1 = Result(78,45,45)


print(r1.phy)
print(r1.calpercentage)

r1.phy = 89

print(r1.phy)
print(r1.calpercentage)




