
import datetime
import math
import fun_otros_datos as val_tipo_vehiculo

lista_vehiculos = []




def agregar_vehiculo():
    print("====== AGREGAR VEHICULO ======\n")
    tipo_vehiculo = val_tipo_vehiculo.validar_tipo_vehiculo
    placa = input("Placa: ")
    hora_ingreso = datetime.datetime.now()
    print("=============================\n")
    
    
    dic_vehiculo = {
        "tipo_vehiculo" : tipo_vehiculo.capitalize(),
        "placa"         : placa.upper(),
        "hora_ingreso"  : hora_ingreso
    }
    
    return dic_vehiculo



def mostar_vehiculos(vehiculos):
    print("=============================")
    for clave, valor in vehiculos.items():
        print(f"{clave} : {valor}")
    print("=============================")
    
    
    
    
def buscar_placa():
    placa_ingresada = input("Placa de vehiculo: ")
        
    for placa in lista_vehiculos:
        if placa_ingresada.upper() == placa["placa"]:
            
            print("\nvehiculo encontrado")
            print("=============================")
            for clave, valor in placa.items():
                print(f"{clave} : {valor}")
            print("=============================")
            
            return placa
        
    return None
            
    
    
    
def cobrar():
    vehiculo_encontrado = buscar_placa()
    
    if vehiculo_encontrado is None:
        print("Vehiculo no encontrado.")
        
    else:
        
        
        hora_entrada = vehiculo_encontrado["hora_ingreso"]

        print("=========================================")
        print("              Parqueadero                ")
        print("=========================================\n")
        print("=============== Salida ==================")
        hora = int(input("Ingrese la hora: "))
        minutos = int(input("Ingrese los minutos: "))
        segundos = int(input("Ingrese la segundos: "))
        print("=========================================\n")


        hora_salida = datetime.datetime(
            hora_entrada.year,
            hora_entrada.month,
            hora_entrada.day,
            hora,
            minutos,
            segundos
        )


        diferencia =  hora_salida - hora_entrada 
        minutos_totales  = math.ceil(diferencia.total_seconds()  / 60)

        total_pagar = minutos_totales * 100


        print("============= Ticket ================")
        print(f"hora de entrada: {hora_entrada.year}-{hora_entrada.month}-{hora_entrada.day} {hora_entrada.hour}:{hora_entrada.minute}:{hora_entrada.second}")
        print(f"hora de salida:  {hora_salida}")
        print(f"minutos totales: {minutos_totales}")
        print(f"Total a pagar: ${total_pagar}")
        print(f"Tipo vehiculo: {vehiculo_encontrado["tipo_vehiculo"]}")
        print(f"Placa: {vehiculo_encontrado["placa"]}")
        
        print("=====================================")
    
    