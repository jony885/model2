dict1={'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
dict2={'x': 300, 'y': 'Red', 'z': 600}
for key in dict1:
    if key in dict2:
        dict1[key]=dict1[key]+dict2[key]
    else:
        pass
l=list(dict1.items())

print(l)
