def test(lst_nt):
    lst=[]
    lst_bsi=[]
    for i in range (len(lst_nt)):
        if lst_nt[i] > 40 :
            lst_bsi.append(lst_nt[i])
    for i in range (len(lst_bsi)):
        if (lst_bsi[i] - 3 )/10> lst_bsi[i] / 10 :
            s=str(lst_bsi[i])
            d=''
            d+=s[0]+'0'
            lst_bsi[i]=int(d)
    return lst_bsi

print(test([30,40,50,83,85]))