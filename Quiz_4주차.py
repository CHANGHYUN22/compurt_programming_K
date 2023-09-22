results = []
b = [90, 45, 64, 9, 17, 29]

for i in b :
    if i >= 90 :
        a = "A"
        results.append(a)
    elif i >= 41 and i < 71 :
        a = "B"
        results.append(a)
    elif i >= 11 and i <41 :
        a = "C"
        results.append(a)
    else :
        a = "D"
        results.append(a)
print(results)
