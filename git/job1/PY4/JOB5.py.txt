def calcule(num1,operator,num2):
    if operator == '+':
        return num1+num2
    if operator == '-':
        return num1-num2
    if operator == '*':
        return num1*num2
    if operator == '/':
        return num1/num2
    if operator == '%':
        return num1%num2

print(calcule(1,'+',8))
print(calcule(1,'-',8))
print(calcule(1,'*',8))
print(calcule(1,'/',8))
print(calcule(3,'%',8))   

