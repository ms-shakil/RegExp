import re
txt = "Bangla english bangla"
match = re.findall("bangla",txt ,re.I|re.M)
print(match)

with open("file.text","r") as f:
    text = f.read()

match = re.findall("^.+",text, re.M)
print(match)    

s = "<li>Tamim</li><li>liton</li><li>shakib</li><li> mahmudullah</li>"
result = re. findall(r'<li>.*</li>', s) # this regexp take all string 
print(result)
result = re.findall(r'<li>(.*?)</li>',s) # this regexp take only names