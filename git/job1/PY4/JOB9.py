def moyenne(nt1,nt2,nt3):
     moy1=0
     moy1=(nt1+nt2+nt3)/3
     return moy1
def job9():
    a=int(input())
    b=int(input())
    c=int(input())
    moyenne_etud=moyenne(a,b,c)
    if moyenne_etud >= 15:
         print("Très bon élève")
    if  11 <= moyenne_etud <= 14 :
        print("Bon élève")
    if  8 <= moyenne_etud <= 10 :
        print("Élève moyen")    
    if  0 <= moyenne_etud <= 8 :
        print("Élève devant faire des efforts")
'''print(job9())'''