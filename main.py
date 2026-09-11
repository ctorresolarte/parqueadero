import menu_principal as menu
import funciones_menu as funciones




while True:

    opcion = menu.menu_principal()
    
    # opcion 1: ingresar carro
    if opcion == 1:
        funciones.lista_vehiculos.append(funciones.agregar_vehiculo())
        print(funciones.lista_vehiculos)
        
    elif opcion == 2:
        for vehiculos in funciones.lista_vehiculos:
            funciones.mostar_vehiculos(vehiculos)
            
    elif opcion == 3:
        funciones.cobrar()
        
        
    elif opcion == 4:
        break