def verificar_primo():
    numero = int(input("Digite un número: "))

    if numero <= 1:
        print("El número ingresado no es primo")
    else:
        es_primo = True

        for divisor in range(2, int(numero**0.5) + 1):
            if numero % divisor == 0:
                es_primo = False
                break

        if es_primo:
            print("El número", numero, "sí es primo")
        else:
            print("El número", numero, "no es primo")

verificar_primo()
