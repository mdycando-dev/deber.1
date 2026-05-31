nombre_usuario = input("Digite su usuario: ")
clave = input("Digite su clave de acceso: ")

if nombre_usuario == "admin" and clave == "123":
    print("Acceso permitido")
    print("Bienvenido al sistema")
else:
    print("Datos incorrectos")
