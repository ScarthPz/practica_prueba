import os
os.system("cls")


trabajador = {}

while True:
    print("""
             - MENÚ -
          1. Registrar Trabajador
          2. Listar los todos los trabajadores
          3. Imprimir planilla de sueldos
          4. Salir del programa""")
    
    while True:
        opc = int(input("Ingrese opción: "))
        if opc in(1,2,3,4):
                    break
        else:
             print("ERROR! vuelva a ingresar opción")

        if opc == 1:
                print("Registrar Trabajador")
                nombre_apellido = input("Ingrese nombre y apellido: ")
                cargo = input("Ingrese cargo: ")
                sueldo_bruto = float(input("Ingrese sueldo bruto: "))

                desc_afp = sueldo_bruto*0.12
                desc_salud = sueldo_bruto*0.07
                total = sueldo_bruto

                trabajador = {
                       
                       "Trabajador": nombre_apellido,
                       "Cargo": cargo,
                       "sueldo Bruto": sueldo_bruto,
                       "Desc. salud": desc_salud,
                       "desc. AFP": desc_afp


                }

        elif opc == 2:
                pass
        elif opc == 3:
                pass
        elif opc == 4:
                print("salir")
                break
                
                
            