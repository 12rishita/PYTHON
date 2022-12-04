# non-homogenous 
# mutable
# items are not duplicated
# ordered
mydict={"Name":"Rishita Chauhan",
"Age":12,
"Age":20,
"Marks":123}
print(mydict)
#get returning the value of particular key
print(mydict.get("Age"))
#keys used for printing all the keys
print(mydict.keys())
print(mydict.values())
#items print list of tuples
print(mydict.items())
#adding item
mydict["Roll no."]=31
mydict["Age"]=21
mydict.update({"Age":23})
mydict.pop("Age")
#pop remove item
#popitem remove last item 
mydict.popitem()
print(mydict)
dict1={"one":1,"two":2,"three":3}
dict2={"four":4,"five":5,"six":6}
#| used for merging 2 dict
# for merging two dict
#dict3=dict1.copy()
#dict3.update(dict2)
print(dict1|dict2)
dict11= {
    "class":{
        "student":{
            "name":"xyz",
            "marks":{
                "python":100,
                "web":90
            }
        }
    }
}
print(dict11["class"]["student"]["marks"]["web"])