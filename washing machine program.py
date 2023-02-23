n=int(input("enter the input"))
if n==0:
    print("time estimated: 0 minutes")
elif n in range(1,2001):
    print("time estimated: 25 minutes")
elif n in range(2001,4001):
    print("time estimated: 35 minutes")
elif n in range(4001,7001):
    print("time estimated: 45 minutes")
else:
    print("invalid output")
