# def add(x,y,z=0):
#     return x+y+z
# print(add(3,4))
# print(add(3,4,5))
class India:
    def capital(self):
        print("New Delhi")
    def language(self):
        print("Hindi")
    def type(self):
        print("Developing")
class USA:
    def capital(self):
        print("Washington DC")
    def language(self):
        print("English")
    def type(self):
        print("Developed")
obj1=India()
obj2=USA()
for i in (obj1,obj2):
    i.capital()
    i.language()
    i.type()
class Bird:
    def wings(self):
        print("Bird has two wings")
    def eyes(self):
        print("Bird has two eyes")
    def fly(self):
        print("Most of the birds can fly")
class Sparrow(Bird):
    def fly():
        print("Saprrow can fly")
class Ostrich(Bird):
    pass
    # def fly(self):
    #     print("Ostrich can't fly")
bird=Bird()
sparrow=Sparrow()
ostrich=Ostrich()
bird.eyes()
bird.wings()
bird.fly()
ostrich.fly()







#Create a car without any variable and methods
class cars:
    pass
car1=cars()
#create a child bus that will inherit all the variable and methods of vehicle class
class vehicle:
    def __init__(self,name,milage):
        self.name = name
        self.milage = milage
class vehicle:
    pass
obj=vehicle(abc)
print(obj.)

