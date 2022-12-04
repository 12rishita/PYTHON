# •	Sets is a non-homogenous but stores in single variable
# •	Representation= {}
# •	no Duplicate element 
# •	unchangeable
#   unordered
#   we can add new item  & remove an item
set={"cars","boat","bike"}
print(set)
#no Duplicate element 
set1={"cars","boat","bike","cars"}
print(set1)
print(len(set))
if "bike" in set:
    print("True")
else:
    print("False")
#add new item
set.add("Cycle")
print(set)
#remove
set.remove('boat')
print(set)
myset1={1,2,3,4}
myset2=set1.union(myset1)#addition of two set & no duplicate item is add
print(myset2)
myset2=set1.intersection(myset1)#common item
print(myset2)
myset2=set1.symmetric_difference(myset1)#do not print common item
print(myset2)
