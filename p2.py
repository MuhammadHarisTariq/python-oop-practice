class Account:
    
    def __init__(self,balance):
        self.mybalance = balance
        
    def withdraw(self,amount):
        self.mybalance -= amount
        print("Your Current Balance After Withdrawal:",self.mybalance)
        
    def deposit(self,amount):
        self.mybalance += amount
        print("Your Current Balance After Deposit:",self.mybalance)
        
    def checkBalance(self):
        print("Your Current Balance:",self.mybalance)
        
        
acc1 = Account(10000)
acc1.deposit(5000)
acc1.withdraw(10000)
acc1.checkBalance()
        
    
        
    
        
        