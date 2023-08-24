import re
def names():
    simple_string = """"Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""")
    pattern="[A-Z{1}]+[a-z{1,}]"
    result = simple_string.replace(",",'').split(" ")
    lstNames=[]
    for name in result:
        if re.search(pattern,name):#finding names and listing them
            lstNames.append(name)
    return lstNames
print(len(names()))
