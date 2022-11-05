#recursion=when a function call itself again and again
#def sum_rec(num):
 #   if num==0:
  #      return num
   # return num+(sum_rec(num-1))
#an=sum_rec(5)
#print(an)

def fac(num):
    if num==0:
        return 1
    return num*(fac(num-1))
an=fac(5)
print(an)