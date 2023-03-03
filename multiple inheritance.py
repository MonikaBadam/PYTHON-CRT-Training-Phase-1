#inheritance

#multiple inheritance

'''class A:
    def m1(self):
        print("in class A")
class B:
    def m1(self):
        print("in class B")

class c(A,B):
    pass
ob=c()
ob.m1()'''

#example:

class lion:
    def m1(self):
        print("singing")
class tiger:
    def m1(self):
        print("crying")

class c(tiger,lion):
    pass
ob=c()
ob.m1()
