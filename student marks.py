class studentmarks:
    def __init__(self):
        self.marks=[]
    def accept(self):
        n=int(input("no of student: "))
        for i in range(n):
            x=int(input("enter student marks: "))
            self.marks.append(x)
        print(self.marks)
    def avg(self):
        total=0
        for x in self.marks:
            total+=x
        avgg=total//len(self.marks)
        return avgg
    def minn(self):
        min=self.marks[0]
        for x in self.marks:
            if x<min:
                min=x
        return min
    def maxx(self):
        max=self.marks[0]
        for x in self.marks:
            if x>max:
                max=x
        return max
    def length(self):
        count=0
        for i in range(len(self.marks)):
            count+=1
        return count
ob=studentmarks()
ob.accept()
while True:
    print('1.avg')
    print('2.min')
    print('3.max')
    print('4.len')
    print('5.exit')
    choice=int(input('enter choice'))
    if choice==1:
        print("avgg: ",ob.avg())
    elif choice==2:
        print("minn: ",ob.minn())
    elif choice==3:
        print("maxx: ",ob.maxx())
    elif choice==4:
        print("length: ",ob.length())
    elif choice==5:
        break
    else:
        print("not valid choice")
