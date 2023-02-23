'''def fun_name(num1,num2):
    print("ans: ", num1+num2)

    fun_name(10, 20, '*')'''

#question:

'''def fun_name(num1,num2,op):
    if op== "+":
        print(num1+num2)
    elif op== "-":
        print(num1-num2)
    elif op== "*":
        print(num1*num2)

fun_name(10, 20, "+")
fun_name(10, 20, "-")
fun_name(10, 20, "*")'''

#method

'''def fun_name(arr):
    arr=[1,2,3,4]
    fun_name(arr)


def arr_sum(a):
    i=0
    for i in range(len(a)):
        sum=0
        sum=sum+i
        print(sum)
a=[1,2,3,4]
arr_sum(a)'''

#return keyword

'''def fun_name(arr):
    sum=0
    for i in range(len(arr)):
        sum=sum+arr[i]
        return sum


arr=[1,2,3,4,5]
ans=fun_name(arr)'''

#regular function

'''def hello(a,b,c):
    print(a)
    print(b)
    print(c)

hello(10,20,30)'''

#default function

'''def hello(a,b,c=0):
    print(a)
    print(b)
    print(c)

hello(10,20)'''


#default function

'''def hello(a=8,b=9,c=0):
    print(a)
    print(b)
    print(c)

hello()'''

#keyword argument function

'''def hello(a,b,c):
    print(a)
    print(b)
    print(c)

hello(a=10,c=20,b=45)'''


#variable length function

'''def hello(*variable):
    print(variable)

hello(10,2,3,4)
hello(10,4,6)'''

#tuple

'''def hello(*variable):
    print(variable)

hello(10,2,3,4)
hello(10,4,6)
hello(100,200,'hello',[1,2,3])'''

def hello(*variable):
    print(variable)

hello(1,2)
hello()
hello(1,2,'hello',[0,2])





















