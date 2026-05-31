def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return None
    return a / b


print("=== MENÚ DE OPERACIONES ===")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = int(input("Elija una opción: "))

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if opcion == 1:
    print("Resultado:", sumar(num1, num2))

elif opcion == 2:
    print("Resultado:", restar(num1, num2))

elif opcion == 3:
    print("Resultado:", multiplicar(num1, num2))

elif opcion == 4:
    resultado = dividir(num1, num2)
    if resultado is None:
        print("No se puede dividir entre cero")
    else:
        print("Resultado:", resultado)

else:
    print("Opción inválida")
