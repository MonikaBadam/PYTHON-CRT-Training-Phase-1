#inheritance

#hierarchy

#example :

class candy:
    name= "candy"

    def method_1(self):
        print("he is a father")

class vandy(candy):
    name= "vandy"

    def method_2(self):
        print("son of candy")

class andy(candy):
    name= "andy"

    def method_3(self):
        print("daughter of candy")

    
class ndy(vandy,andy):
    pass

ob=ndy()
ob.method_1()
ob.method_2()
ob.method_3()

