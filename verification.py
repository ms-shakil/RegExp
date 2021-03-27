import re
# phone number verification

num = "Hi my name is fahad . my phone number is 01725698745 . Hi my name is  sajjad . my phone number is 01934568795"
numer = re.findall(r"01[3-9]\d{8}",num)
print(numer)


# # gmail verification
inp = input("Enter your Gmail:")
gmail = re.search("\w+@\w+\.\w{3,5}",inp)
if gmail != None:
    print("Congratulations ! your gmail is verificate.")
else:
    print("Your Enter Wrong Gmail.")    
