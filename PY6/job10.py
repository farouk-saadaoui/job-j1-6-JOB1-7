def produit(lst):
    prod=1
    for i in range (len(lst)):
        if 90 >lst[i] >=25 :
            prod=prod * lst[i]
    return prod

print(produit([1,89,25,3,4]))