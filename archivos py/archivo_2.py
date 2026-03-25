contraseña_guardada=int(input("ingrese una contraseña:"))
contraseña_ingresada=1234
clave_token=bool(input("usa clave token? "))
if contraseña_guardada==contraseña_ingresada:
    print("acceso con clave")
elif clave_token == "si":
    print("acceso permitido")
else:
    print("acceso denegado")
