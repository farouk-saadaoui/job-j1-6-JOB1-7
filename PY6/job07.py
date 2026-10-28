def compte(lst):
    cpt=0
    for i in range(len(lst)):
        if lst[i] % 3 == 0 :
            cpt+=1
    return cpt

print(compte([8, 24,48,2,16]))