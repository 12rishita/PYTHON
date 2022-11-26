
#List are used to store multiple non-homogeneous data in a single variable
#Changeable or mutable
#duplicate variable
#inserts-it inserts new objects in the list at particular index
#append- it inserts object at the end of the list
#extend-adds one list to another list (it can be used to add different collection like tuple
#remove-removes item from specified index
#pop- removes from particular index if index not mentioned then removes the last object
#clear- it clears the list (prints the empty list)
#del(variable)- deletes object of particular index
#sort- helps to arrange the objects in ascending order(<)
#sort(reverse True)- prints in descending order


#cl=['Red','Green','Yellow','Blue','White']
#print(cl)
#b=['Red','Green','Yellow','Blue','White',12,13]
#print(b[0:4])
#l=['Red','Green','Yellow','Blue','White']
#l[3]=23
#print(l)
#l[1]="Black"
#print(l)
#colors=['Red','Blue','Red','Black',22]
#colors[0:2]=['Yellow','Pink']
#colors[0]='Yellow'
#colors[1]='Pink'
#######    INSERT OBJECT BEFORE INDEX
#colors=['Red','Blue','Red','Black',22]
#colors.insert(1,"Indigo")
#colors.append("BMw")

#print(colors+cars)
#colors.extend(cars)
#colors.extend(players)

#colors.remove("Red")
#colors.pop(1)
#colors.clear()
colors=['Red','Blue','Red','Black',22]
cars=['TATA','Nano','BMW',"Jeep","Alto"]
players=['Shreyas Iyer',"Rohit",'Neymar','Messi']
#low=[x.lower() for x in cars]
#print(low)
#newlist=[x for x in cars if x=="TATA"]
#     "x" iS EXPRESSION ITEM
#print(newlist )
#for x in players:
 #   print(x)
#for x in range(len (players)):
 #   print(players (x) )
#x=0
#while x < len(players):
#    print(players[x])
#for direct     [print (x) for x in players]
#newlist=[]
#for i in cars:
 #   if 'A' in i:
  #      newlist.append(i)
#print(newlist)
#=[1,2,3,4,5]
#new=[]
#for i in num:
 #   i=i*i
  #  new.append(i)
#print(new)
#num.sort(reverse=2)
#print(num)
#cars.sort()
#print(cars)
#new_list=[ x*x for x in num]
#print(new_list)
#number=[1,2,3,4,5,2,6]
#a=number.index(2)
#number[a]=200
#print(number)
#n1=[]
#for j in range(len(number)):
#    if number[j]==2:
 #       number[j]=200
#print(number)
#newlist=players.copy()
#print(newlist)
#new2=list(number)
#print(new2)
list1=['x','y','z']
list2=[1,2,3]
print(list1+list2)
#list1.append(list2)
#print(list1)
for x in list2:
    list1.append(x)
print(list1)