list1=[3,4,10,9,18,66,13,15]
evenno=list(filter(lambda i : i%2==0,list1))
print(evenno)
#filter 
#map does operation on each item of the list
sq=list(map(lambda i : i**2,list1))
print(sq)

list2=[10,20,30,40,50]
tr=list(map(lambda i:i*3,list2))
print(tr)
#list3=["a","B","c","D","e","f"]

#li=list(map(lambda i:    ,list3 ))
#print(li)-
def div(a,b):
    print(a/b)
def good_div(fun):
    def inner_div(a,b):
        if a<b:
            a,b=b,a
        return fun(a,b)
    return inner_div
output=good_div(div)
div(2,4)