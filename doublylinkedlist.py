class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Doublylinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertbegin(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
    def insertEnd(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.prev=self.tail
            self.tail.next=newNode
            self.tail=newNode
    def search(self, key):
        if self.head is None:
            print("DLL is empty")
            return

        temp = self.head
        position = 1

        while temp:
            if temp.data == key:
                print(f"{key} found at position {position}")
                return
            temp = temp.next
            position += 1

        print(f"{key} not found")

    
    def delbegin(self):
        if self.head is None:
            print("DLL is empty")
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            self.head.prev=None
            del temp
    def delEnd(self):
        if self.head is None:
            print("DLL is empty")
        else:
            temp=self.tail
            self.tail=self.tail.prev
            temp.prev=None
            self.tail.next=None
            del temp
    
    def display(self):
        if self.head is None:
            print("DLL is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=' ')
                temp=temp.next

DLL=Doublylinkedlist()
DLL.display()
DLL.insertbegin(10)
DLL.insertbegin(20)
DLL.insertbegin(30)
DLL.insertbegin(40)
print()
DLL.display()
DLL.insertEnd(200)
print()
DLL.display()
print()
DLL.delbegin()
DLL.display()
DLL.search(20)
DLL.search(2000)
print()
