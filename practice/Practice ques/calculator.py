import math 
print(""" 
press -  
1 - Addition(x, y) 
2 - Subtraction(x,y) 
3-  Multiplication(x,y) 
4 - Division(x, y) 
5- Exponent(x, y) 
6 - tan(x, y) 
7 - sin(x) 
8 - cos(x) 
9 - Factorial(x) 
10 - log(x) 
11 - Round off
""") 
num= input("") 
if num== "1": 
    x = int(input("1st number -")) 
    y = int(input("2nd number -")) 
    print(x + y) 
elif num == "2": 
    x = int(input("1st number -")) 
    y = int(input()) 
   
    print(x-y) 
elif num == "3": 
    x = int(input("1st number -")) 
    y = int(input("2nd number -")) 
    print(x*y) 
elif num== "4": 
    x = int(input("1st number -")) 
    y = int(input("2nd number -")) 
    print(x/y) 
elif num == "5": 
    x = int(input("1st number -")) 
    y = int(input("2nd number -")) 
    print(x**y) 
elif num == "6": 
    x = int(input("1st number -")) 
    y = int(input("2nd number -")) 
    print(math.tan(x)) 
elif num == "7": 
    x = int(input("Enter your number=")) 
     
    print(math.sin(x)) 
elif num== "8": 
    x = int(input("Enter your number=")) 
    print(math.cos(x))
elif num == "9": 
    x = int(input("Enter your number=")) 
    print(math.factorial(x)) 
elif num == "10": 
    x = int(input("Enter your number=")) 
    print(math.log(x))
elif num=="11":
    x = float(input("Enter your number=")) 
    print(round(x,2)) 