opciones = 0
salir = 0
nomusu1 = 0

#Base de vehículos
vehiculos = []

#Función para mostrar el inventario por sede
def inventario_sedes(sede):
    #Variable para determinar si hay en la sede
    paso = "no"
    
    print("\nLos vehículos de la sede", sede, "son:\n")
    
    largo = len(vehiculos)#Toma lo largo de la matriz
    #Recorre las filas
    for vehiculo in range(largo):
        #Compara las  sede
        if(vehiculos[vehiculo][8] == sede):
            paso = "si"#Indica que si hay vehiculos en esa sede
            print("Marca:", vehiculos[vehiculo][0])
            print("Modelo:", vehiculos[vehiculo][1])
            print("Año:", vehiculos[vehiculo][2])
            print("Cilindraje:", vehiculos[vehiculo][3])
            print("Precio de alquiler por día:", vehiculos[vehiculo][4])
            print("Precio:", vehiculos[vehiculo][5])
            print("Placa:", vehiculos[vehiculo][6])
            estado = "Disponible" if not vehiculos[vehiculo][7] else "Inhabilitado"
            print("Estado:", estado)
            print("Sede:", vehiculos[vehiculo][8])
            print()

    #Mensaje de que no hay sedes
    if(paso == "no"):
        print("No hay vehículos en esta sede\n")
            

#Función para ingresar a una sede
def sedes():
    salir = "no"#Variable que determina cuando salir del ciclo
    while(salir == "no"):
        print("Ingrese a la sede a la que gusta ingresar: ")
        print("1 - San José")
        print("2 - Alajuela")
        print("3 - Guanacaste")
        print("4 - Limón")
        print("5 - Puntarenas")
        print("6 - Pérez Zeledón")
        print("7 - Salir")
        sede = input(">>")

        if(sede == "1"):
            print("\nBienvenido a la sede de San José")
            print("Nuestro horario de atención son las 24 horas todos los días\n")

            sal = "no"#Variable que determina cuando salir del ciclo
            while(sal == "no"):
                print("1 - Visualizar vehículos \n2 - Reservar Vehículo \n3 - Salir")
                op = input(">>")

                if(op == "1"):
                    inventario_sedes("San José")
                elif(op == "2"):
                    print("Esta opción está en mantenimiento")
                elif(op == "3"):
                    print("Usted saldrá correctamente")
                    sal = "si"
                else:
                    print("Ingrese un valor correcto")
            
        elif(sede == "2"):
            print("\nBienvenido a la sede de Alajuela")
            print("Nuestro horario de atención son las 24 horas todos los días\n")

            sal = "no"#Variable que determina cuando salir del ciclo
            while(sal == "no"):
                print("1 - Visualizar vehículos \n2 - Reservar Vehículo \n3 - Salir")
                op = input(">>")

                if(op == "1"):
                    inventario_sedes("Alajuela")
                elif(op == "2"):
                    print("Esta opción está en mantenimiento")
                elif(op == "3"):
                    print("Usted saldrá correctamente")
                    sal = "si"
                else:
                    print("Ingrese un valor correcto")
                    
        elif(sede == "3"):
            print("\nBienvenido a la sede de Guanacaste")
            print("Nuestro horario de atención es de 4:00 am a 11:00 pm\n")

            sal = "no"#Variable que determina cuando salir del ciclo
            while(sal == "no"):
                print("1 - Visualizar vehículos \n2 - Reservar Vehículo \n3 - Salir")
                op = input(">>")

                if(op == "1"):
                    inventario_sedes("Guanacaste")
                elif(op == "2"):
                    print("Esta opción está en mantenimiento")
                elif(op == "3"):
                    print("Usted saldrá correctamente")
                    sal = "si"
                else:
                    print("Ingrese un valor correcto")
                    
        elif(sede == "4"):
            print("\nBienvenido a la sede de Limón")
            print("Nuestro horario de atención es de 6:00 am a 10:00 pm\n")

            sal = "no"#Variable que determina cuando salir del ciclo
            while(sal == "no"):
                print("1 - Visualizar vehículos \n2 - Reservar Vehículo \n3 - Salir")
                op = input(">>")

                if(op == "1"):
                    inventario_sedes("Limón")
                elif(op == "2"):
                    print("Esta opción está en mantenimiento")
                elif(op == "3"):
                    print("Usted saldrá correctamente")
                    sal = "si"
                else:
                    print("Ingrese un valor correcto")
                    
        elif(sede == "5"):
            print("\nBienvenido a la sede de Puntarenas")
            print("Nuestro horario de atención es de 5:00 am a 10:00 pm\n")

            sal = "no"#Variable que determina cuando salir del ciclo
            while(sal == "no"):
                print("1 - Visualizar vehículos \n2 - Reservar Vehículo \n3 - Salir")
                op = input(">>")

                if(op == "1"):
                    inventario_sedes("Puntarenas")
                elif(op == "2"):
                    print("Esta opción está en mantenimiento")
                elif(op == "3"):
                    print("Usted saldrá correctamente")
                    sal = "si"
                else:
                    print("Ingrese un valor correcto")
                    
        elif(sede == "6"):
            print("\nBienvenido a la sede de Pérez Zeledón")
            print("Nuestro horario de atención es de 7:00 am a 10:00 pm\n")

            sal = "no"#Variable que determina cuando salir del ciclo
            while(sal == "no"):
                print("1 - Visualizar vehículos \n2 - Reservar Vehículo \n3 - Salir")
                op = input(">>")

                if(op == "1"):
                    inventario_sedes("Pérez Zeledón")
                elif(op == "2"):
                    print("Esta opción está en mantenimiento")
                elif(op == "3"):
                    print("Usted saldrá correctamente")
                    sal = "si"
                else:
                    print("Ingrese un valor correcto")
                    
        elif(sede == "7"):
            print("Usted regresará al menú")
            salir = "si"
        else:
            print("Ingrese un valor correcto")

def listar_vehiculos(vehiculos):
    if len(vehiculos) == 0:
        print("No hay vehículos en el inventario.")
    else:
        print("Listado de vehículos en inventario:")
        for vehiculo in vehiculos:
            print("Marca:", vehiculo[0])
            print("Modelo:", vehiculo[1])
            print("Año:", vehiculo[2])
            print("Cilindraje:", vehiculo[3])
            print("Precio de alquiler por día:", vehiculo[4])
            print("Precio:", vehiculo[5])
            print("Placa:", vehiculo[6])
            estado = "Disponible" if not vehiculo[7] else "Inhabilitado"
            print("Estado:", estado)
            print("Sede:", vehiculo[8])
            print()

#Función que busca la placa del vehículo
def buscar_placa(vehiculos, placa):
    largo = len(vehiculos)#Toma lo largo de la matriz
    #Recorre las filas
    for fila in range(largo):
        #Compara las placas
        if(vehiculos[fila][6] == placa):
            return True

#Función para ingresar un vehículo
def gestion_inventario(vehiculos):
    print("Gestión de inventario")
    print("Agregar inventario\n")

    # Variables para el ingreso como administrador
    admin = "admin"
    contraadmin = "contra"

    # Solicitud de credenciales de administrador
    print("Ingrese el usuario de administrador: ")
    user = input(">>")
    print("Ingrese la contraseña de administrador: ")
    password = input(">>")

    # Inicio de sesión como admin
    if(user == admin and password == contraadmin):
        print("Inicio de sesión correcto\n")

        # Variables
        marca = "indefinido"
        anio = 0
        modelo = "indefinido"
        cilindraje = 0
        precio_de_alquiler = 0
        precio = 0
        placa = "indefinido"
        inhabilitado = False
        cantidad_de_vehículos = 0
        sede = "indefinido"

        # Variable para determinar cuando termina el ciclo
        i = "si"

        # Ciclo de solicitud de datos del vehículo
        while i == "si" or i == "SI" or i == "Si":
            print("Ingrese la marca del vehículo: ")
            marca = input(">>")
            print("Ingrese el modelo del vehículo: ")
            modelo = input(">>")

            # Solicitud de cantidad de vehículos de marca y modelo
            print("Ingrese la cantidad de vehículos que requiere agregar de ese modelo: ")
            cantidad_de_vehículos = input(">>")
            cantidad_de_vehículos = int(cantidad_de_vehículos)

            # Ingresa la cantidad de vehículos
            for j in range (cantidad_de_vehículos):
                print("Ingrese el año del vehículo", marca, modelo, "número #", j + 1)
                anio = input(">>")
                print("Ingrese el cilindraje del vehículo", marca, modelo, "número #", j + 1)
                cilindraje = input(">>")
                print("Ingrese el precio del alquiler por día del vehículo", marca, modelo, "número #", j + 1)
                precio_de_alquiler = input(">>")
                print("Ingrese el precio del vehículo", marca, modelo, "número #", j + 1)
                precio = input(">>")

                #Determina si ya está la placa en la matriz
                determinante = False
                while(determinante == False):
                    print("Ingrese la placa del vehículo", marca, modelo, "número #", j + 1)
                    placa = input(">>")

                    if(buscar_placa(vehiculos, placa) == True):
                        print("La placa ya se encuentra en el sistema")
                        determinante = False
                    else:
                        determinante = True

                #Menú para ingresar la sede
                valido = "no"
                while(valido == "no"):
                    print("Ingrese la sede del vehículo", marca, modelo, "número #", j + 1)
                    print("-> San José (1), Alajuela (2), Guanacaste (3), Limón (4), Puntarenas (5) o Pérez Zeledón (6)")
                    sede = input(">>")

                    #Condicional para guardar la sede
                    if(sede == "1"):
                        sede = "San José"
                        valido = "si"
                    elif(sede == "2"):
                        sede = "Alajuela"
                        valido = "si"
                    elif(sede == "3"):
                        sede = "Guanacaste"
                        valido = "si"
                    elif(sede == "4"):
                        sede = "Limón"
                        valido = "si"
                    elif(sede == "5"):
                        sede = "Puntarenas"
                        valido = "si"
                    elif(sede == "6"):
                        sede = "Pérez Zeledón"
                        valido = "si"
                    else:
                        print("Ingrese un valor valido")
                        valido == "no"

                # Guarda en la matriz los datos del vehículo
                vehiculos.append([marca,modelo,anio,cilindraje,precio_de_alquiler,precio,placa,inhabilitado,sede])

            # Determina si se continúa en el ciclo
            print("¿Desea seguir ingresando vehículos? si/no")
            i = input(">>")
            if(i == "no" or i == "No" or i == "NO"):
                print("Usted regresará al menú\n")
            elif(i == "si" or i == "Si" or i == "SI"):
                print("Ingrese un nuevo Vehículo")
            else:
                print("Ingrese un valor correcto")
                i = "si"
    else:
        print("\nIngrese el usuario y contraseña correctos\n")
        
while True:

    inises=input("Bienvenido desea: \n Crear un Usuario(1) \n Iniciar Sesión(2) \n Ingresar como Invitado (3) \n Ingresar Inventario (4) \n Visualizar Inventario(5) \n")
    print(" ")


    if inises=="1":
        nomusu1=str(input("Ingrese el nombre de usuario que desea utilizar:"))
        print(" ")
        contra1=str(input("Ingrese la contraseña que desea utilizar:"))
        print(" ")
        deseoini=str(input("Usuario registrado con exito, desea iniciar sesion(si)(no)?"))

        if deseoini=="si":
            print(" ")
            inicio_sesion_usu1=str(input("Ingrese su nombre de usuario: "))
            print(" ")

            if inicio_sesion_usu1==nomusu1:
                print(" ")
                inicio_sesion_contra1=str(input("Ingrese su contrasena:"))
                print(" ")
                
                if inicio_sesion_contra1==contra1:
                    print(" ")
                    print("Inicio de sesion exitoso")
                    print(" ")

                    opciones = int(input("Desea gestionar el inventario (1) ver los vehiculos disponibles(2) ingresar sede(3) o salir (4)?"))
                if opciones == 1:
                    #Gestion Inventarios
                    gestion_inventario(vehiculos)
                    
                elif opciones== 2:
                    #Visualizar vehiculos
                    listar_vehiculos(vehiculos)

                elif opciones== 3:
                    #Invoca la función de sedes
                    sedes()
                    
                elif opciones == 4:
                    salir = str(input("Si desea salir digite ´si´, en el caso contrario digite ´no´"))
                    
                    if salir == "si" or salir == "SI" or salir == "Si" or salir == "sI":

                        print("Adios, gracias por su visita!")

                        break
                            

                    elif salir == "no" or salir == "NO" or salir == "No" or salir == "nO":

                        print("Como desee")

                elif inicio_sesion_contra1 != contra1:
                    print(" ")
                    print("La contrasena ingresada no es valida")
                    print(" ")
                    
            elif inicio_sesion_usu1 != nomusu1:
                print(" ")
                print("El usuario ingresado no esta registrado")
                print(" ")
                
        elif deseoini=="no":
                print("")


    elif inises=="2":
        
        inises_nomusu1=str(input("Ingrese su usuario: "))
        if inises_nomusu1!= nomusu1:
            print(" ")
            print("El nombre de usuario no esta registrado")
            print(" ")
        elif inises_nomusu1==nomusu1:
            print(" ")
            inises_contra1=str(input("Ingrese su contrasena: "))
            print(" ")
            if inises_contra1==contra1:
                print(" ")
                print("Inicio de sesion exitoso")
                print(" ")

                opciones = int(input("Desea gestionar el inventario (1) ver los vehiculos disponibles(2) ingresar sede(3) o salir (4)?"))
                if opciones == 1:
                    gestion_inventario(vehiculos)




                elif opciones == 2:
                    #Visualizar vehiculos
                    listar_vehiculos(vehiculos)
                    
                    salir = str(input("Si desea salir digite ´si´, en el caso contrario digite ´no´"))
                    
                    if salir == "si" or salir == "SI" or salir == "Si" or salir == "sI":

                        print("Adios, gracias por su visita!")

                        break
                            

                    elif salir == "no" or salir == "NO" or salir == "No" or salir == "nO":

                        print("Como desee")

                elif opciones== 3:
                    #Invoca la función de sedes
                    sedes()
                    

                elif opciones == 4:
                    salir = str(input("Si desea salir digite ´si´, en el caso contrario digite ´no´"))
                    
                    if salir == "si" or salir == "SI" or salir == "Si" or salir == "sI":

                        print("Adios, gracias por su visita!")

                        break
                            

                    elif salir == "no" or salir == "NO" or salir == "No" or salir == "nO":

                        print("Como desee")




        else:
            print(" ")
            print("No existe ningun usuario registrado")
            print(" ")

    elif inises == "3":
        eleccion_invitado=int(input("Visualizar inventario,iniciar sesion y salir"))
        if eleccion_invitado==1:
            listar_vehiculos(vehiculos)
        elif eleccion_invitado==2:
            print("")
            print("al iniciar como usuario invitado no tiene el mismo poder que a uno registrado")
            print("Los usuarios registrados")
            print("")    
        elif eleccion_invitado==3:
            print("adios")
       

        cambio = str(input("Desea iniciar sesión (si) o (no):"))
        
        if cambio == "si" or cambio == "Si" or cambio == "SI":
            
            inises_nomusu1=str(input("Ingrese su usuario: "))
            if inises_nomusu1!= nomusu1:
                print(" ")
                print("El nombre de usuario no esta registrado")
                print(" ")
            elif inises_nomusu1==nomusu1:
                print(" ")
                inises_contra1=str(input("Ingrese su contrasena: "))
                print(" ")
                if inises_contra1==contra1:
                    print(" ")
                    print("Inicio de sesion exitoso")
                    print(" ")

            opciones = int(input("Desea gestionar el inventario (1) Ver los vehiculos disponibles(2) o salir (3)?"))
            if opciones == 1:
                #Gestion Inventarios
                gestion_inventario(vehiculos)
                
            elif opciones == 2:
                #Visualizar vehiculos
                listar_vehiculos(vehiculos)
          
                
            elif opciones == 3:
                salir = str(input("Si desea salir digite ´si´, en el caso contrario digite ´no´"))

                if salir == "si" or salir == "SI" or salir == "Si" or salir == "sI":

                    print("Adios, gracias por su visita!")

                    break
                    

                elif salir == "no" or salir == "NO" or salir == "No" or salir == "nO":

                    print("Como desee")

                
        elif cambio == "no" or cambio == "No" or cambio == "NO":
            
            print("Su ingreso ha sido exitoso")

    elif inises == "4":
        #Visualizar vehiculos
        gestion_inventario(vehiculos)
        
    elif inises == "5":
        #Visualizar vehiculos
        listar_vehiculos(vehiculos)
          
    else:
        print("El valor ingresado no pertenece a un opcion")
        break
