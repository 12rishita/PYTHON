#prime no
num1=int(input("Starting="))
num2=int(input("Ending="))
for i in range (num1,num2+1):
    if i >1:
        for n in range(2,i):
            if(i%n)==0:
                break
        else:
            print(i)