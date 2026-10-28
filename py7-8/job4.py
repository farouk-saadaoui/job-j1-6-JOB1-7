def cesar(msg,dec):
    alpha="abcdefghijklmnopqrstuvwxyz"
    reponse=""
    for e in msg:
        for i in range(len(alpha)):
            if e == alpha[i] :
                if i+dec > 25 :
                    reponse+=alpha[(i+dec)-25]
                else :
                    reponse+=alpha[i+dec]
    return reponse

print(cesar('abc',3))