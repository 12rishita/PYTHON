#Square root a number
num=int(input("Enter a number="))
a=num**0.5
print(a)

#Area of a triangle
s1=float(input("Side 1="))
s2=float(input("Side 2="))
s3=float(input("Side 3="))
sum=(s1+s2+s3)/2
area=(sum*(sum-s1)*(sum-s2)*(sum-s3))**0.5
print("Area of a triangle=",area)

