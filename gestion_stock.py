stock_productoso = { "enlatados": [],
"frutas": [],
 "congelados": [],
"panaderia": []
} 
stock_cantidad = { "enlatados": [],
 "frutas": [],
  "congelados": [],
 "panaderia": []
} 

def iniciar():
    for categoria in stock_productoso:
        stock_productoso = []
def cargar_stock(): 
    categoria = input("ingresa la categoria")
    if categoria in stock_productoso:
      productito = input("ingresa el nombre del producto")
      cant = int(input("ingresa la cantidad"))
      stock_productoso[categoria].append(productito)
      stock_cantidad[categoria].append(cant)
      print("producto cargado")
    else:
        print("la categoria no esta")
def muestra_stock(): 
 print (" productos:")
 print (stock_productoso)
 print ("cantidad del product")
 print (stock_cantidad)  
def contar(lista_productos):
    cantidad_items = 0
    suma_total = 0
    for elemento in lista_productos:
     suma_totale = suma_totale + elemento
     cantidad_items = cantidad_items + 1
    print("cantidad de productos distintos")
    print(cantidad_items)
    print("suma total:")
    print(suma_totale)
    
    
 
 
    
    



    
    
    
