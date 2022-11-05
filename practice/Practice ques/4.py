#FIBONACCI SERIES
num=int(input("Start="))
n1,n2=0,1
count=0
if num<=0:
    print()
elif num==1:
    print()
    print(n1)
else:
    while count<num:
        print(n1)
        sum=n1+n2
        n1=n2
        n2=sum
        count+=1