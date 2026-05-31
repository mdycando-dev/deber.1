saldo_cuenta = 1000

while True:

    print("\n===== CAJERO AUTOMÁTICO =====")
    print("1 -> Ver saldo")
    print("2 -> Sacar dinero")
    print("3 -> Ingresar dinero")
    print("4 -> Terminar")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("Saldo disponible:", saldo_cuenta)

    elif opcion == 2:
        monto_retiro = float(input("¿Cuánto desea retirar?: "))

        if monto_retiro <= 0:
            print("El valor ingresado no es válido")

        elif monto_retiro > saldo_cuenta:
            print("Fondos insuficientes")

        else:
            saldo_cuenta = saldo_cuenta - monto_retiro
            print("Retiro realizado correctamente")
            print("Saldo restante:", saldo_cuenta)

    elif opcion == 3:
        monto_deposito = float(input("Ingrese el monto a depositar: "))

        if monto_deposito > 0:
            saldo_cuenta += monto_deposito
            print("Depósito realizado")
            print("Saldo actualizado:", saldo_cuenta)
        else:
            print("No puede ingresar valores negativos")

    elif opcion == 4:
        print("Sesión finalizada")
        break

    else:
        print("Opción incorrecta, intente otra vez")
