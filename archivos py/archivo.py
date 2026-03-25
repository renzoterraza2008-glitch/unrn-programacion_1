
contraseña_guardada=int(input("ingrese una contraseña:"))
contraseña_ingresada=int(input("ingrese su contraseña guardada:"))
if contraseña_ingresada==contraseña_guardada:
    acceso_permitido = True
    print("tu acceso fue concebido")
elif contraseña_guardada!=contraseña_ingresada:
    acceso_permitido = False
    print("tu acceso fue denegado")
    if acceso_permitido==True:
        print("gracias por usar nuestro sistema seguro")







