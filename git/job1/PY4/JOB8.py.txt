def tp(type,saison):
    if type == 'fruits' and saison== 'hiver' :
        print("orange, mandarine et kiwi")
    if type == 'fruits' and saison== 'ete' :
            print("Poire, fraise, cassis")
    if type == 'legume' and saison== 'hiver' :
            print("carotte, topinambour, endive")
    if type == 'legume' and saison== 'ete' :
            print("artichaut, aubergine,navet")
print(tp('fruits','hiver'))
print(tp('fruits','ete'))
print(tp('legume','hiver'))
print(tp('legume','ete'))
