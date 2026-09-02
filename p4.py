class A:
     var1 = "this is class A"
     
class B:
    var2 = "this is class B"
    
class C(A,B):
    var3 = "this is class C"
    
myobj = C()

print(myobj.var1)
print(myobj.var2)
print(myobj.var3)