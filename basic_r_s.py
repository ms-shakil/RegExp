# find  land or lands endswith country with normal code 
S="Afganistan,America,Bangladesh,Canada,Denmark,England,Greenland,Iceland,Netherland,New Zealand,Sweden,Switzerland"
country =S.split(",")
li = [item for item in country if item.endswith("land") or item.endswith("lands")]
print(li)



#### use regexp
# find  land or lands endswith country with regexp

import re
s="Afganistan,America,Bangladesh,Canada,Denmark,England,Greenland,Iceland,Netherland,New Zealand,Sweden,Switzerland"
li = re.findall("\w+lands*",s)
print(li)


#########  find  string to other string  by search function

match = re.search("bangla","bangladesh") # search return obj
print(match.group()) # group mathods return finding string

####### use .   . meaning every character
bd = "Bangladesh"
match = re.search(".",bd)
print(match.group())
match = re.search("B.n",bd)
print(match.group())
match = re.search("B.n...",bd)
print(match.group())
bd = "Bangladesh is our country"
match = re.search("............",bd)
print(match.group()) # . take character and space  . its meaning (.) take evey thing with out new line and \n

########### \w  (\w)meaning all [A-Z a-z 0-9 _]
bd = "Bangladesh is our homeland"
match = re.search("o\w\w",bd)
print(match.group()) 
match = re.search("i\w\w",bd)
print(match)
match = re.search("B\w+h",bd)
print(match.group())
match = re.search("B.+h",bd) ## "B.+h " meaning start B  ending last h  ........not end first and mid h
print(match.group())
match = re.search("B.+?h",bd)
print(match.group())


########## \d  (\d)meaning [0-9] 
text = "Phone number: 01789399861"
match = re.search("\d+",text)
print(match.group())

text = "House number:5 , phone number: 01789399861"
match = re.search("\d+",text) # it dosen't find phone number its find  5
print(match.group()) 
match = re.search('\d{11}',text)
print(match.group())

text = "017 89399861"
match = re.search('\d{3}\s\d{8}',text) # \s meaning space 
print(match.group())