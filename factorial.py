def comprobar_numero():

    valor = int(input("Ingrese un número entero: "))

    if valor < 2:
        print("No es un número primo")

    else:
        primo = True

        for num in range(2, valor):
            if valor % num == 0:
                primo = False

        if primo:
            print(valor, "es primo")
        else:
            print(valor, "no es primo")

comprobar_numero()
