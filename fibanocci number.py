a=0
b=1
i=1
value=int(input("enter range vaule"))
x=[0,1]
while i<=value-2:
    result=a+b
    x.append(result)
    a=b
    b=result
    i=i+1
print(x)

