def cm(n,s=10000):
    print("The Salary of",n,"is",int(s))
cm("Ben",12000)
cm("Mike",15000)
cm("Bob",)


def de(name,*data):
    print(name)
    print(data)
de("Rishita",Place="Shimla",Age=19,No=7474748392)

def de(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
de("Rishita",place='Shimla',age=19,no=5678765)
