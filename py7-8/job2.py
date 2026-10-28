def triangle(inp):
    for i in range(inp+1):
        print(" ",end='')
    print("/",end='')
    print("\\")
    for j in range(inp):
        for d in range(inp):
            print(" ",end='')
        print("/",end='')
        for d in range(inp-3):
            print("\\",end='')
    
        







       ###for i in range(inp*2):
        ###if i==inp :
           ## print("/",end='')
            ##print("\\")
        ##if i==spe :
         ##   print('\\' ) 
        ##for j in range(6):
          ##  spe+=1
            ##if j==spe :
              ##  print('/')
            ##if j==spe+1:
              ##  print('\\' )   """
print(triangle(5))  