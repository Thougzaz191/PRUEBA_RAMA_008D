#calculadora
a = int(input(""))
b = int(input(""))
print ("1.SUMA")
print ("2.RESTA")
op = int(input("Elige una opcion"))

def suma (a,b):
    if op == "1": 
        resultado = a + b
        return resultado
    elif op == "2":
        resultado = a - b
        return resultado

print(suma(a,b))

print("caquita")