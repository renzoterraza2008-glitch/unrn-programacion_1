# numero=-1

# while numero < 0:
#     numero= int(input("ingresar un numero valido: "))
    
# print("numero valido de ingreso")

opcion = "" 
total = 0 
print("Selecciona la comida para llevar)")

while opcion != "terminar pedido":
    opcion = input("Escriba la comida que quieras agregar al pedido: ").lower()
    if opcion == "pizza":
        total += 25 
        print("ok agregamos una pizza ")
    elif opcion == "hamburguesa":
        total += 20
        print("ok agregamos una hamburguesa ")
    elif opcion == "empanada":
        total += 15
        print("ok agregamos una docena de empanadas ")
    elif opcion == "coca-cola":
        total += 10
        print("ok agregamos una coca-cola")
    elif opcion == "terminar pedido":
        print("Pedido cerrado")
    else:
        print(f"Lo siento, no tenemos {opcion}, prueba con otra cosa")

print(f"Pedido finalizado el total a pagar es: ${total}")














