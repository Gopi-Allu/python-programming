num=int(input("enter a number:"))
sum=0
pro=1
temp=num
while temp>0:
    rem=temp%10
    sum=sum+rem
    pro=pro*rem
    temp=temp//10
if(sum==pro):
    print("spy number")
else:
    print("not a spy number")
