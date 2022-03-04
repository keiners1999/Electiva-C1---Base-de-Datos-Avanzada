from cgi import print_arguments


def Triangulo(a,b):
    area = (base*altura)/2
    return f"El area de su triangulo es==> {area:.0f} "

base = float(input("ingrese la base del triangulo ==> "))
altura = float(input("ingrese la altura del triangulo ==> "))
print(Triangulo(base,altura))


