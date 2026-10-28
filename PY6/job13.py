def supprime():
    lst=[10, 20,
30, 20, 10, 50, 60, 40, 80, 50, 40]
    d=dict()
    d[lst[-1]]=1
    dd=-1
    while lst[-1] != lst[0] :
        dd-=1
        for key in d :
            if lst[dd] == key :
                pass
            if  lst[dd] != key :
                d[lst[dd]]=1     
    lsttt=[]
    i=0        
    for keys in d :
        lsttt+=keys
        i+=1
    return lsttt
print(supprime())