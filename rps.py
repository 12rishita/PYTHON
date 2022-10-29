from random import random


import random
user=input("Enter your choice (Rock,Paper,Scissors)=")
comp=['Rock','Paper','Scissors']
ac=random.choice(comp)
print("Computer choice=",ac)
if user==ac:
    print("Tie")
elif user=="Rock" and ac=="Scissors":
    print("User WON")
elif user =="Paper" and ac=="Rock":
    print("User won")
elif user=="Scissors" and ac=="Paper":
    print("User Won")
else:
    print("Computer WON")

