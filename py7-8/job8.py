def my_sort(lst):
    cpt=0
    for i in range(0,len(lst)-1):
            if lst[i+1] < lst[i]  :
                tem=lst[i]
                ten=lst[i+1]
                lst[i+1]=tem
                lst[i]=ten
                
                cpt+=1
    
    print(f"nombre total de coups necessaire pour trier la liste : {cpt} \n Liste Triee : {lst}")
print(my_sort([99,22,10,6,34,64,90]))  
