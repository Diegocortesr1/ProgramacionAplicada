a = input("Ingrese el numero a: ")
a = int(a)
b = input("Ingrese el numero b: ")
b = float(b)
c = a + b
if a == b:
    print("Igual")
else:
    print("Diferente")
print("a es de tipo: ", type(a))
print("b es de tipo: ", type(b))
print("c = ", c)
if type(a) == type(b):
    print("a y b son del mismo tipo")
else:
    print("a y b son de diferente tipo")