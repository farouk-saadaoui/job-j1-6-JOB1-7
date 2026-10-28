def cm(nb_marche,hauteur):
    res=0
    res=(5*hauteur*nb_marche*2*7)
    print(f'Pour {nb_marche} marches de {hauteur} cm, le gardien parcourt {res/100} m par semaine.')
print(cm(10,10))