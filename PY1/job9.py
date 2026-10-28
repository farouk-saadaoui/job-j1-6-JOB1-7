def gestion():
    name='produit'
    price=4
    quantit=0
    print(f'le {name} a {price} euro en quantite de :{quantit}')
    quantit+=10
    print(f'le {name} a {price} euro en quantite de :{quantit}')
    c=int(input('saisir la quantité de produits qu’il souhaite acheter'))
    quantit=quantit-c
    price=price*1.1
    print(f'le {name} a {price} euro en quantite de :{quantit}')
    
print(gestion())