# values defined-attribute
#class ---template
#object is made to use template
class Laptop:
    def __init__(self):
        print("Hello Rishita")
    def config(self):
        print("Asus","i7","1TB")

laptop1=Laptop()
laptop2=Laptop()
#Laptop.config(laptop1)
laptop1.config()
laptop2.config()