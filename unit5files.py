f=open("demo.txt","r")
#f=open("demo.txt","r",encoding="utf-8")
#print(f.read())
#print(f.readline())
#print(f.readline())

f1=open("demo1.txt","w")
#create file automatically
f1.write("This is a new file.\n")
f1.write("This is a random file.\n")
for i in f:
    f1.write(i)
# f2=open("My Self.txt","w")
# f2.write("My name is Rishita Chauhan.\n")
# f2.write("I am from Shimla.\n")
# f2.write("I am a Student.\n")
# f2.write("I am doing B.Tech CSE.\n")