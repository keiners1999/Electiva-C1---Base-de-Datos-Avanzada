a = float(input("por favor darle valor 'a' ==> "))
b = float(input("por favor darle valor 'b' ==> "))
c = float(input("por favor darle valor 'c' ==> "))
d = (b**2)-4*a*c

if d < 0:
    print("el resultado es indefinido")
else:
    print(f"el resultado de su ecuacion - es: {(-b-(d)**1/2)/(2*a)}")
    print(f"el resultado de su ecuacion + es: {(-b+(d)**1/2)/(2*a)}")