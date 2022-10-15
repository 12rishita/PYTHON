y=int(input("Time spend in company="))
s=int(input("Current salary="))
if y>10:
    a=s+(10/100)*s
    print("Bonus will be=",a)
elif y>=6 and y<10:
    b=s+(8/100)*s
    print("Bonus will be=",b)
elif y<6:
     c=s+(5/100)*s
     print("Bonus will be=",c)
else:
    print (s)

