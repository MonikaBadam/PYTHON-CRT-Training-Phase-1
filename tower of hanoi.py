def hanoi(n, a, b, c):
    if n>0:
        hanoi(n-1,a,c,b)
        if n==1:
            b.append(a[-1])
            a.remove(a[-1])
            print('a, c, b :{}\t{}\t{}'.format(a,b,c))
        else:
            hanoi(n-1,a,b,c)
            hanoi(1,a,c,b)
            hanoi(n-1,c,a,b)
n=3
a=list(range(n,0,-1))
b,c=[],[]
hanoi(n-1,a,b,c)

'''def hanoi(n, a, b, c):
    if n>0:
        hanoi(n-1,a,c,b)
        if a:
            b.append(a[1])
            a.remove(a[1])
            print('a, c, b :{}\t{}\t{}'.format(a,b,c))
        else:
                hanoi(n-1,a,b,c)
                hanoi(1,a,c,b)
                hanoi(n-1,c,a,b)
n=4
a=list(range(n,0,-1))
b,c=[],[]
hanoi(n-1,a,b,c)'''


