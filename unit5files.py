# f=open("demo.txt","r")
# print(f.read(5))
# #f=open("demo.txt","r",encoding="utf-8")
# #print(f.read())
# #print(f.readline())
# #print(f.readline())

# f1=open("demo1.txt","w")
# #create file automatically
# f1.write("This is a new file.\n")
# f1.write("This is a random file.\n")
# for i in f:
#     f1.write(i)
# f2=open("My Self.txt","w")
# f2.write("My name is Rishita Chauhan.\n")
# f2.write("I am from Shimla.\n")
# f2.write("I am a Student.\n")
# f2.write("I am doing B.Tech CSE.\n")
# try:
#     f=open("demo.txt")
#     #your codes goes here
# finally:
#     f.close()
#this way we are making sure that file is closed properly even if raised that cause the program flow to stop. 
# with open("demo.txt") as f:
#     f.read() #-->example
#     #your codes goes here
#tell
# print(f.tell())
# f=open("bg.jpg","rb")
# # print(f.read())
# f1=open("bg_copy.jpg","wb")
# # print(f.read())
# for i in f:
#     f1.write(i)
#_----------------------removing file
# import os 
# os.remove("demo1.txt")
# import os
# if os.path.exists("demo1.txt"):
#     os.remove("demo1.txt")
# else:
#     print("File does not exist")