def ech(tab):
    temp=tab[0]
    tab[0]=tab[-1]
    tab[-1]=temp
    return tab  
print(ech([1,2,3,4,5]))