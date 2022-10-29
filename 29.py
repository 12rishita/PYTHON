#take user input(string)
#if the len of string is greater than 3
# add "ing" as a suffix in the the original string
# else print the same string given by user
st=str(input("Input="))
if len(st)>3:
    print(st+'ing') 
else:
    print(st)