dic = {1: 'Lee', 2: 'Kim', 3: 'Park'}
print(dic)
print(a := dic.keys())
print(b := dic.values())

print(type(a))
print(dic.get(1))
for k in a:
    print(k, dic[k])