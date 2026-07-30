class bank:
    name=None
    accno=None
    
    def accept(self):
        self.name=input("enter your name: ")
        self.accno=int(input("enter account number: "))
        self.balance=0
    def depoist(self):
        self.dptamt=int(input("enter depoist amount: "))
        self.balance+=self.dptamt
        return self.balance
    def withdrawal(self):
        self.wtd=int(input("enter withdrawal amount: "))
        if self.wtd<=self.balance:
            self.balance-=self.wtd
        else:
            print("insufficienr balance")
    def display(self):
        print(self.balance)
        
s1=bank()
s1.accept()
s1.depoist()
s1.withdrawal()
s1.display()
