class bill:
    n=None
    fbill=0
    def accept(self):
        self.n=int(input("enter the number of products: "))
        self.total=0
        for i in range(self.n):
            price=int(input("enter the product price: "))
            self.total+=price
        return self.total
    def calc(self):
        x=self.accept()
        if self.total>=1000:
            self.disc=self.total*0.1
        elif self.total>=500:
            slef.disc=self.total*0.05
        else:
            self.disc=0
        self.finalbill=self.total-self.disc
    def display(self):
        print(self.finalbill)
s1=bill()
s1.calc()
s1.display()
        
        





   
