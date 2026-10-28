def simu():
    montant_ini=10000
    taux_de_rendement=4
    print(f"le gain annuel={montant_ini*(1+taux_de_rendement/100)} ")
    montant_ini+=5000
    taux_de_rendement+=2
    print(f"le gain annuel={montant_ini*(1+taux_de_rendement/100)} ")
    montant_ini=montant_ini*0.9
    taux_de_rendement-=1
    print(f"le gain annuel={montant_ini*(1+taux_de_rendement/100)} ")
print(simu())