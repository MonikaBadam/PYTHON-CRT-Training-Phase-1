#inheritance

#single level

#example 1:

'''class parent:
    name= "parent class"

    def method_1(self):
        print("this is method of class A")


class child(parent):
    pass

ob = child()
print(ob.name)
ob.method_1()'''


#example 2:

class vehicle:
    name= "vehicle"

    def method_1(self):
        print("my fav vehicle is bmw")


class car(vehicle):
    pass

ob = car()
print(ob.name)
ob.method_1()
