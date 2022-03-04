def ConReturn(a,b):
    return (f"el resultado de su ecuacion es: {pow((a**2)+(b**2),1/3)}")
    
a = float(input("por favor darle valor 'a' ==> "))
b = float(input("por favor darle valor 'b' ==> "))    
print(ConReturn(a,b))