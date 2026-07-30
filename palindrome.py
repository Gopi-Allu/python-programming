num=int(input("enter a number:"))
rev=0
temp=num
while temp>0:
    rem=temp%10
    rev=rev*10+rem
    
    temp=temp//10
if(rev==num):
    print("palindrome number")
else:
    print("not a palindrome number")

