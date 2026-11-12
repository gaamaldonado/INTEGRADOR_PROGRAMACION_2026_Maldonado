import menu 
import gestion_stock 
def main ():
    gestion_stock.iniciar()
    opcion = menu.mostrar_menu
    if opcion == 1: 
     gestion_stock.cargar_stock
     if opcion == 2: 
         gestion_stock.muestra_stock
    elif opcion == 3 :
       categori_contar = input("ingresa la categoria que queres contar")
    if categori_contar in gestion_stock.stock_cantidadd:
     lista_contar = gestion_stock.stock_cantidad[categori_contar]
     gestion_stock.contar(lista_contar) 
               
    if __name__ == "__main__": 
     main()