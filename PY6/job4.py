def lst():
    lst=["pomme","cerise","orange","Melon"]
    lst.insert(2,"mangue")
    return lst

def lssst():
    lst=["pomme","cerise","orange","Melon"]
    s=[]
    for i in range (1,len(lst)):
        if i == 2 :
            s.append("mangue")
        else :
            s.append(lst[i])
    return s
 
print(lssst())
    