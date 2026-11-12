stock_productoso = {
    "enlatados": [],
    "frutas": [],
    "congelados": [],
    "panaderia": []
}
stock_cantidad = {
    "enlatados": [],
    "frutas": [],
    "congelados": [],
    "panaderia": []
}
def iniciar():
    for categoria in stock_productoso:
        stock_productoso[categoria] = []
    for categoria in stock_cantidad:
        stock_cantidad[categoria] = []
def cargar_stock():
    categoria = input("ingresa laq categoria ")
    if categoria in stock_productoso:
        productito = input("ingresa el nombre del producto ")
        cant = int(input("ingresa la cantidadd "))
        stock_productoso[categoria].append(productito)
        stock_cantidad[categoria].append(cant)
        print("producto cargado")
    else:
        print("la categoria no esta")
def muestra_stock():
    print("productos")
    print(stock_productoso)
    print("cantidad del producto")
    print(stock_cantidad)
def contar(lista_productos):
    cantidad_items = 0
    suma_total = 0
    for elemento in lista_productos:
        suma_total = suma_total + elemento
        cantidad_items = cantidad_items + 1
    print("cantidad de productos distintos")
    print(cantidad_items)
    print("suma total")
    print(suma_total)
 
 
    
    



    
    
    
