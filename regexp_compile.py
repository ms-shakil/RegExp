import re
text = "This is line . Date is 2021/02/21. And theres is another date: 2021-03-21. The Third and final dae is 2022/05/22."
date = re.compile(r"\d{4}[-/]\d{2}[-/]\d{2}") # complile regexp
result = date.findall(text)
print(result)

### american number verifiction with using compile
num = "415-555-4242"
number = re.compile(r"\d{3}-\d{3}-\d{4}")
result  = number.findall(num)
print(result)

