def ConRetorno(a,b,c):
    d =  pow((b**2)-4*a*c,1/2)

    if d < 0:
        return "el resultado es indefinido"
    else:
        return (f"el resultado de su ecuacion + es: {(-b+pow((b**2)-4*a*c,1/2))/(2*a)}"+
    f"\nel resultado de su ecuacion - es: {(-b-pow((b**2)-4*a*c,1/2))/(2*a)}")

a = float(input("ingrese el valor de 'a' ==> "))
b = float(input("ingrese el valor de 'b' ==> "))
c = float(input("ingrese el valor de 'c' ==> "))

print(ConRetorno(a,b,c))