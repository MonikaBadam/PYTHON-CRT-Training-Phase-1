#series
 
n=int(input("enter the nth series"))
if n%2==0:
    n=n//2
    print(n*6)
else:
    n=n//2+1
    print(n*7)
 
