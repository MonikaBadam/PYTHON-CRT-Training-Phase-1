a,b,c=int(input("enter the value of a")),int(input("enter the value of b")),int(input("enter the value of c"))

temp=a
a=b
b=c
c=temp
s=(a+b+c)/2
d=(s*(s-a)*(s-b)*(s-c))**0.5
print(d)
print(type(d))
