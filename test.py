data=[1,10,3,4,5,6,7,8]
text=""
tem=5
for value in data:
    if value>tem:
        text+="[-],"
    else:
        text+="[+]"
print(text)