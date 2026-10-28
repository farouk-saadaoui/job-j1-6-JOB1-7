def max_min1(lst):
    max=lst[0]
    for  i in range (1,len(lst)):
        if lst[i] >= max :
            max=lst[i]
    min=lst[i]
    for i in range (1,len(lst)):
        if lst[i] <= min :
            min=lst[i]
    print(f"la valeur max est : {max}\nla valeur min est : {min}")

print(max_min1([8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]))