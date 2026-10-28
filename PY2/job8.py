def tour2():
    precedent=0
    for i in range (1,13):
        precedent+=2
        print(f"Tour{i}: {precedent} ")
print(tour2())
    
        