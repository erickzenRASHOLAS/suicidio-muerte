from funciones import *

while True:
    os.system('cls')
    print("\t BIENVENIDO :)")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar Sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir")
    opc=str(input("INGRESE UNA OPCIÓN: "))
    os.system('cls')

    
    
    if opc=="1":
        Asignar_sueldos()
    elif opc=="2":
        Clasificar_sueldos()
    elif opc=="3":
        ver_estadísticas()
    elif opc=="4":
        Reporte_sueldos()
    elif opc=="5":
       print("Finalizando programa")
       time.sleep(1) 
       print("Desarrollado por Erick Rosales")
       time.sleep(2)
       print(" RUT 22.013.437-7")
       time.sleep(2) 
       print(" HATSA LUEGO <3 :)")
       time.sleep(1) 
       break
    else:
        print("ERROR!!! DEBE INGRESAR UNA OPCIÓN VALIDA!!!!")
        time.sleep(3)
