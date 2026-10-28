def tour():
    precedent=1
    print(f"Tour {1}: {precedent}")
    for i in range(2,11):
        print(f"Tour {i}: {i*3 -2}")
print(tour())