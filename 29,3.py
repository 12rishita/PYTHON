#Accept a number from the user calculate and print the sum of all no. from 1 to input no. using FOR LOOP
num=int(input("Enter any number="))
sum=0
for i in range (1,num+1):
    sum=sum+i
print("Sum=",sum)

#for i in range(num):
#         sum=sum+i+1