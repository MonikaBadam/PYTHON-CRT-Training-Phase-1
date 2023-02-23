#strings basic format

'''txt='moni'
index=0
for i in txt:
    print("message[", index,"]= ",i)
    index+=1'''

#string functions

#title

'''txt='jersey'
print(txt.title())'''

#upper

'''txt='nani'
print(txt.upper())'''

#lower

'''txt='SUNNY'
print(txt.lower())'''

#zero fill
                                                                   
'''txt='6'
print(txt.zfill(4))'''

#lstrip

'''txt= ' hi students'
print(txt.lstrip())'''

#armstrong number

'''n=int(input("enter a number"))
s=0
while(n!=0):
    r=n%10
    s=s+(r*r*r)
    s+=(r*r*r)
    n=n//10
if (s==n):
    print("armstrong number")
else:
    print("not an armstrong number")'''

#max element

'''txt= 'glucosez'
print(max(txt))'''

#replace element

'''txt='vandy'
print(txt.replace('v', 'c'))'''

#swap case

'''txt='MONI CANDY'
print(txt.swapcase())'''

#split

'''txt='moni,navi,candy '
print(txt.split(','))'''

#join

'''print('-'.join(['m','n','c']))'''

#enumerate

'''txt='my name is mimni'
print(list(enumerate(txt)))'''

#alphanumeric

'''txt='jersey004'
print(txt.isalnum())'''

#numeric

'''txt='jersey004'
print(txt.isnumeric())'''

#upper

'''txt='jersey004'
print(txt.isupper())'''

#lower

'''txt='jersey004'
print(txt.islower())'''

#space

'''txt='jersey004'
print(txt.isspace())'''

#length

'''txt='jersey004'
print(len(txt))'''

#right

'''txt="monika"
print(txt.ljust(10,'*'))'''

#left

'''txt="monika"
print(txt.rjust(10,'*'))'''

#center

'''txt="monika"
print(txt.center(12,'*'))'''


