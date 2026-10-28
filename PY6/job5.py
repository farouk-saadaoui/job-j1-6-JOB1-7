def l():
    L=[i for i in range(1,6)]
    print(L)
    print(L[1])
    def remplace():
        L[3]=L[2]+L[4]
        print(L)
    remplace()
    print(L[-1])
print(l())