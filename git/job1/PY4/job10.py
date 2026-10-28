def job10(nb):
    if type(nb) == int :
        if nb >= 0:
            if nb%2==0:
                return True
            else : 
                return False
        else :
            return ' introduire un nb possitif'
    else :
        return 'introduire un nb entier et possitif'
print(job10(3))
print(job10(3.3))
print(job10(-3))