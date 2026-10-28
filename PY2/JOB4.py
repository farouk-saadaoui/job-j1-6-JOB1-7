def multiplication():
    x=int(input("entrer un nombre sup a zero(N)"))
    print(f"table de multiplication de {x}")
    for i in range (1,11):
        print(f"{x} x {i} = {i*x}")
print(multiplication())