# # try:
# #     #this block of code will run and throw errors if there any
# # except:
# #     #this will raise the errors
# # else:
# #     #this will execute if there are no errors
# finally:
#     #this will execute regardless the result of try and except
"""try:
    f=open("demo.py")
    try:
        f.write("ABC")
    except:
        print("Error in the file")
    finally:
        f.close()
except:"""

a = 5
if a<20:
    raise Exception("Value is less than 5")

