import menu
import gestion_stock
def main():
    gestion_stock.iniciar()
    opcion = 0
    while opcion != 4 :
        opcion = menu.mostrar_menu()
        
        if opcion == 1:
            gestion_stock.cargar_stock()
        elif opcion == 2:
            gestion_stock.muestra_stock()
        elif opcion == 3:
            categori_contar = input("ingresa la categoria que queres contar: ")
            if categori_contar in gestion_stock.stock_cantidadd:
                lista_contar = gestion_stock.stock_cantidad[categori_contar]
                gestion_stock.contar(lista_contar)
            else:
                print("esa categoria no existe")
        elif opcion == 4:
            print("programa finalizado")
        else:
            print("opcion no valida")
if __name__ == "__main__":
    main()
