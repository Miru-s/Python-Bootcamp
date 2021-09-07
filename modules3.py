import re

text= "The rain in Mumbai is so beautiful"
x= re.findall("Mumbai",text)
print(x)

if(x):
    print("Found a match")
else:
    print("No match found")

y = re.search("\s", text)
print("The first white-space character is located in position:", y.start())

z=re.split("\s", text)
print(z)

w=re.sub("\s", " *** ", text)
print(w)