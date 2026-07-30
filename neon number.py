num=int(input("enter a number:"))
sum=0
sqr=num**2
while sqr>0:
    rem=sqr%10
    sum=sum+rem
    sqr=sqr//10
if(sum==num):
    print("neon number")
else:
    print("not a neon number")


