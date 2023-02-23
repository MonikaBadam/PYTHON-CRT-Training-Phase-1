#numbers side by side

'''num=int(input("enter the number"))
#initialization
i=0
while(i<=num):#condition
    print(i,end="")
    i=i+1 #increment'''

#numbers one by one

'''num=int(input("enter the number"))
#initialization
i=0
while(i<=num):#condition
    print(i)
    i=i+1 #increment'''

#sum of "n" numbers

'''num=int(input("enter the number"))
#initialization
i=sum=0
while(i<=num):
    sum=sum+i
    i=i+1
    print(sum)'''

#add all digits in a number

'''num=int(input("enter the number"))
i=sum=0
while(num!=0):
 r=num%10
 sum=sum+r
 num=num//10
print(sum)'''

#even numbers

'''num=int(input("enter the number"))
i=0
while(i<=num):
   if i%2==0:
       print(i,end="\t")
   i=i+1'''

#sum of n even numbers

'''num=int(input("enter the number"))
i=sum=0
while(i<=num):
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum)'''

#sum of n odd numbers

'''num=int(input("enter the number"))
i=sum=0
while(i<=num):
    if i%2!=0:
        sum=sum+i
    i=i+1
print(sum)'''

#sum of odd and even numbers

#method1:

'''num=int(input("enter the number"))
i=sum=0
while(i<=num):
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum of even)
num=int(input("enter the number"))
i=sum=0
while(i<=num):
    if i%2!=0:
        sum=sum+i
    i=i+1
print(sum)'''

#method2:

'''num=int(input("enter number"))
i=o=e=0
while(i<=num):
    if i%2==0:
        e=e+i
    else:
        o=o+i
    i=i+1
print("even sum is",e)
print("odd sum is",o)'''

#reverse the numbers 

'''num=int(input("enter number"))
temp=0
while(num!=0):
    temp=num%10
    print(temp,end="")
    num=num//10'''

#decimal to binary

'''dn=int(input("enter number"))
bn=0
i=0
while dn!=0:
    r= dn%2
    bn= bn+r*(10**i)
    dn=dn//2
    i+=1
print(bn)'''

#binary to decimal

#method1:

'''bn=int(input("enter number"))
dn=0
i=1
while bn!=0:
    r=bn%10
    dn=dn+(r*i)
    bn=int(bn/10)
    i=i*2
print(dn)'''

#method2:

'''bn=int(input("enter number"))
dn=0
i=0
while bn!=0:
    r= bn%10
    dn= dn+r*(2**i)
    bn=bn//10
    i+=1
print(dn)'''





