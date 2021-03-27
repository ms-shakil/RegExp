import re
text = """  thamaite parte na
    kew thamaite parbe na
    kew thamaite parbe na """

subtt = re. sub(r'thamaite','thabraite',text, re.M)
print(subtt)  

## find word on string with 
text = "hi this is sajjad. i am a software engineer ! . now i am working on google . Do you know about me?"
subs = re.sub(r"[.!?]"," ",text)
print(len(subs.split()))

text = "Hi This is payer . i am a software engineer. I was working on Handymama as a software engineer."
chg= re. sub(r'software','civil',text , re.M)
print(chg)
