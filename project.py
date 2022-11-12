print(""" Press -  
0 - Addition(num1+num2) 
1 - Subtraction(num1-num2) 
2-  Multiplication(num1*num1) 
3 - Division(num1/num2) 
4  - Modulus (num1%num2)
5- Exponent(num1**num2) 
""") 
x=int(input("Enter your choice="))
def n(num1,num2):
    if x==0:
        print(num1+num2)
    elif x==1:
        print(num1-num2)
    elif x==2:
        print(num1*num2)
    elif x==3:
        print(num1/num2)
    elif x==4:
        print(num1%num2)
    elif x==5:
        print(num1**num2)
n(112,90)