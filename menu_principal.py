def menu_principal():
    while True:
        print("======= MENU PRINCIPAL ======\n")
        print("1. Ingresa Vehiculo")
        print("2. Mostrar")
        print("3. Cobrar")
        print("4. Salir")
        print("=============================\n")
        
        try:
            opc = int(input("Seleccione una opcion para continuar:  "))
            print()
            
            if 1 <= opc <= 4:
                return opc
            else:
                print("Opcion invalida, intente nuevamente.")
        except ValueError:
            print("Debe seleccionar un numero entero para continuar: \n") 
            
    


                 
                 
                 