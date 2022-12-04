#tuples store multiple items in a single variable
#ordered,unchangeable,  
my_tuple=("orange")
print(my_tuple)
my_tuple1=("orange",)
print(my_tuple1)
my_tuple2=("orange","apple","pineapple","grapes")
print(my_tuple2)
print(my_tuple2[1])
print(my_tuple2[-1])
print(my_tuple2[0:])
#ques
l=list(my_tuple2)
print(l)
#l.pop()
l.append("APPLE")
t=tuple(l)
print(t)
#adding tuple
tuple1=(1,2,3)
tuple2=(4,5,6)
tuple1+=tuple2
print(tuple1)
#revese the above tuple
t=tuple1[::-1]
print(t)
#tuple name
name=("Rishita",)
print(name)
#packing & unpacking
tup=("A","B","C")
(one,*two,three)=tup  #8 is taking all the parameter and leaving one for one parameter
print(one)
print(two)
print(three)
#write a program to unpack the following tuple  into four variable and print each variable
tu=("RED","Yellow","White","Blue")
(one,two,three,four)=tu
print(one)
print(two)
print(three)
print(four)