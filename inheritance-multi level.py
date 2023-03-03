#inheritance

#multi level

'''class A:
    var1="in class A"
class B(A):
    var2="in class B"
class c(B):
    var3="in class C"
class D(C):
    var4="in class D"'''



#example

class CANDY:
    name= "CANDY"

    def method_1(self):
        print("my best frnd")

        
class MIMNI(CANDY):
    name= "MIMNI"

    def method_2(self):
        print("i am his best frnd")

class MONIKA(MIMNI):
    pass

ob=MIMNI()
print(ob.name)
ob.method_1()
ob.method_2()
    
