class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stackLL:
    def __init__(self):
        self.top=None
    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False
    def Push(self,data):
        newnode=node(data)
        if self.isEmpty():
            self.top=newnode
        else:
            newnode.next=self.top
            self.top=newnode
    def pop(self):
        if self.isEmpty():
            return -1
        else:
            delnode=self.top
            popped=delnode.data
            self.top=self.top.next
            delnode.next=None
            del delnode
            return popped
    def peek(self):
        if self.isEmpty():
            return -1
        else:
            return self.top.data
    def display(self):
        if self.isEmpty():
            print("st is empty")
        else:
            temp=self.top
            while temp:
                print(temp.data)
                print('--------')
                temp=temp.next
        print()
    def search(self,target):
        if self.isEmpty():
            print("empty")
        else:
            temp=self.top
            while temp:
                if temp.data==target:
                    print("found")
                    break
                else:
                    temp=temp.next
            else:
                print("not found")

s1=stackLL()
while True:
    print('--operations---')
    print('1.PUSH')
    print('2.POP')
    print('3.Peek')
    print('4.display')
    print('5.search')
    print('6.exit')
    option=int(input("enter operation: "))
    if option==1:
        ele=int(input("enter ele:"))
        s1.Push(ele)
    elif option==2:
        res=s1.pop()
        if res!=-1:
            print(f'Popped:{res}')
        else:
            print("underflow")
    elif option==3:
        res=s1.peek()
        if res==-1:
            print("underflow")
        else:
            print(f'top ele is:{res}')
    elif option==4:
        s1.display()
    elif option==5:
        target=int(input("search for:"))
        s1.search(target)
    elif option==6:
        break
    else:
        print("enter valid option")
                  
                  

