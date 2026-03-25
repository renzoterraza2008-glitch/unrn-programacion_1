lista_super= ["huevos", "pan", "coca", "azucar", "leche", "fideos"]

indice=0
while indice < len(lista_super):
    print(indice, lista_super[indice])
    indice+=1
while True:
    indice_selecionado=int(input("elegi la comida"))
    if indice_selecionado < len(lista_super):
        comida=lista_super[indice_selecionado]
        print(f"elegiste el indice {indice_selecionado}: {comida}")
    else:
        print("elegiste una comida invalida")







