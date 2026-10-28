def somme(lst):
    s=0
    for i in range(len(lst)):
        s+=lst[i]

    return s 

print(somme([8, 24,48,2,16]))
print(somme([10,2,16]))