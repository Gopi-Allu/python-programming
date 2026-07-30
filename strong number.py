sum=0
num=int(input("enter a number:"))
temp=num
while temp>0:
    i=1
    fact=1
    rem=temp%10
    while i<=rem:
        fact=fact*i
        i=i+1
    sum=sum+fact
    temp=temp//10
if sum==num:
    print("strong number")
else:
    print("not strng number")
