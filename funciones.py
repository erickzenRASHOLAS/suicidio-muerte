import os
import random
import time
import csv

aleatorio1=random.randint(300000,2500000)
aleatorio2=random.randint(300000,2500000)
aleatorio3=random.randint(300000,2500000)
aleatorio4=random.randint(300000,2500000)
aleatorio5=random.randint(300000,2500000)
aleatorio6=random.randint(300000,2500000)
aleatorio7=random.randint(300000,2500000)
aleatorio8=random.randint(300000,2500000)
aleatorio9=random.randint(300000,2500000)
aleatorio10=random.randint(300000,2500000)
sueldos=[]
sueldos.append(aleatorio1)
sueldos.append(aleatorio2)
sueldos.append(aleatorio3)
sueldos.append(aleatorio4)
sueldos.append(aleatorio5)
sueldos.append(aleatorio6)
sueldos.append(aleatorio7)
sueldos.append(aleatorio8)
sueldos.append(aleatorio9)
sueldos.append(aleatorio10)

datos_trabajadores=[]
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez",
                "Laura Hernández","Miguel Sánchez","Isabel Gómez",
                "Francisco Díaz","Elena Fernández"]
datos_trabajadores.append(trabajadores)


#funciones principales:

def Asignar_sueldos():
    
    print("SUELDOS ASIGNADOS CON EXÍTO")
    time.sleep(3)

def Clasificar_sueldos():
    time.sleep(2)
    print("SUELDOS MENORES A $800.000 TOTAL: ?")
    print("SUELDOS ENTRE $800.000 $2.000.000 TOTAL: ?")
    print("SUELDOS SUPERIORES A $2.000.000")
    total_sueldos=aleatorio1+aleatorio2+aleatorio3+aleatorio4+aleatorio5+aleatorio6+aleatorio7+aleatorio8+aleatorio9+aleatorio10
    print(f"TOTAL SUELDOS: {total_sueldos}")
    time.sleep(4)
def ver_estadísticas():
    
    time.sleep(2)
    promedio=(aleatorio1+aleatorio2+aleatorio3+aleatorio4+aleatorio5+aleatorio6+aleatorio7+aleatorio8+aleatorio9+aleatorio10)/10
    media_geométrica=(aleatorio1*aleatorio2*aleatorio3*aleatorio4*aleatorio5*aleatorio6*aleatorio7*aleatorio8*aleatorio9*aleatorio10)**(1/10)
    print(f"PROMEDIO: {promedio}, MEDIA GEOMÉTRICA: {media_geométrica}")
    time.sleep(3)
def Reporte_sueldos():
    
    time.sleep(2)

    dcto_salud1=int(aleatorio1*0.07)
    dcto_afp1=int(aleatorio1*0.12)
    
    sueldo_li1=aleatorio1-(dcto_salud1+dcto_afp1)
    print(f"NOMBRE EMPLEADO |SUELDO BASE |DCTO SALUD |DCTO AFP |SUELDO LIQUIDO")
    print(f"{trabajadores[0]}\t {aleatorio1}\t{dcto_salud1}\t  {dcto_afp1}\t{sueldo_li1}")

    dcto_salud2=int(aleatorio2*0.07)
    dcto_afp2=int(aleatorio2*0.12)
    sueldo_li2=aleatorio2-(dcto_salud2+dcto_afp2)
    print(f"{trabajadores[1]}\t {aleatorio2} \t{dcto_salud2} \t  {dcto_afp2} \t{sueldo_li2}")
    
    dcto_salud3=int(aleatorio3*0.07)
    dcto_afp3=int(aleatorio3*0.12)
    sueldo_li3=aleatorio3-(dcto_salud3+dcto_afp3)
    print(f"{trabajadores[2]}\t {aleatorio3} \t{dcto_salud3}\t  {dcto_afp3} \t{sueldo_li3}")
    
    dcto_salud4=int(aleatorio4*0.07)
    dcto_afp4=int(aleatorio4*0.12)
    sueldo_li4=aleatorio4-(dcto_salud4+dcto_afp4)
    print(f"{trabajadores[3]}\t {aleatorio4} \t{dcto_salud4}\t  {dcto_afp4} \t{sueldo_li4}")
    
    dcto_salud5=int(aleatorio5*0.07)
    dcto_afp5=int(aleatorio5*0.12)
    sueldo_li5=aleatorio5-(dcto_salud5+dcto_afp5)
    print(f"{trabajadores[4]}\t {aleatorio5} \t{dcto_salud5}\t  {dcto_afp5} \t{sueldo_li5}")

    dcto_salud6=int(aleatorio6*0.07)
    dcto_afp6=int(aleatorio6*0.12)
    sueldo_li6=aleatorio6-(dcto_salud6+dcto_afp6)
    print(f"{trabajadores[5]}\t {aleatorio6} \t{dcto_salud6}\t  {dcto_afp6} \t{sueldo_li6}")

    dcto_salud7=int(aleatorio7*0.07)
    dcto_afp7=int(aleatorio7*0.12)
    sueldo_li7=aleatorio7-(dcto_salud6+dcto_afp7)
    print(f"{trabajadores[6]}\t {aleatorio7} \t{dcto_salud7}\t  {dcto_afp7} \t{sueldo_li7}")

    dcto_salud8=int(aleatorio8*0.07)
    dcto_afp8=int(aleatorio8*0.12)
    sueldo_li8=aleatorio8-(dcto_salud8+dcto_afp8)
    print(f"{trabajadores[7]}\t {aleatorio8} \t{dcto_salud8}\t  {dcto_afp8} \t{sueldo_li8}")

    dcto_salud9=int(aleatorio9*0.07)
    dcto_afp9=int(aleatorio9*0.12)
    sueldo_li9=aleatorio9-(dcto_salud9+dcto_afp9)
    print(f"{trabajadores[8]}\t {aleatorio9} \t{dcto_salud9}\t  {dcto_afp9} \t{sueldo_li9}")

    dcto_salud10=int(aleatorio10*0.07)
    dcto_afp10=int(aleatorio10*0.12)
    sueldo_li10=aleatorio10-(dcto_salud10+dcto_afp10)
    print(f"{trabajadores[9]}\t {aleatorio10} \t{dcto_salud10}\t  {dcto_afp10} \t{sueldo_li10}")
    
   
    if not "reporte sueldos.csv":
        with open ("reporte sueldos.csv","x", newline="") as file:
            lector=csv.DictWriter(file,[trabajadores])
            print("CSV CREADO!")
            time.sleep(25)
            pass
    else:
        print("ERROR EL ARCHIVO YA EXISTE!!")
        time.sleep(25)