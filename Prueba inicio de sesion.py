
opciones = 0
salir = 0
nomusu1 = 0

#Base de vehículos
vehiculos = []


while True:

    inises=input("Bienvenido desea, crear un usuario(1) / iniciar sesion(2) / ingresar como invitado (3) / visualizar inventario")
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

                    opciones = int(input("Desea gestionar el inventario (1) o desea salir (2)?"))
                if opciones == 1:

                    #Gestión de inventario

                    print("Gestión de inventario")
                    print("Agregar inventario\n")

                    #Variables para el ingreso como administrador
                    admin = "admin"
                    contraadmin = "contra"

                    #Solicitud de credenciales de admimnistrador
                    print("Ingrese el usuario de administrador: ")
                    user = input(">>")
                    print("Ingrese la contraseña de administrador: ")
                    password = input(">>")

                    #Inicio de sesión como admin
                    if(user == admin and password == contraadmin):

                        print("Inicio de sesión correcto\n")

                        #Variables
                        marca = "indefinido"
                        anio = 0
                        modelo = "indefinido"
                        cilindraje = 0
                        precio_de_alquiler = 0
                        precio = 0
                        placa = "indefinido"
                        inhabilitado = False
                        cantidad_de_vehículos = 0

                        #Variable para determinar cuando termina el ciclo
                        i = "si"

                        #Ciclo de solicitud de datos del vehículo
                        while i == "si" or i == "SI" or i == "Si":
                            
                            #Pide marca y modelo
                            print("Ingrese la marca del vehículo: ")
                            marca = input(">>")
                            print("Ingrese el modelo del vehículo: ")
                            modelo = input(">>")

                            #Solicitus de cantidad de vehículos de marca y modelo
                            print("Ingrese la cantidad de vehículos que requiere agregar de ese modelo: ")
                            cantidad_de_vehículos = input(">>")
                            cantidad_de_vehículos = int(cantidad_de_vehículos)

                            #Ingresa la cantidad de vehículos
                            for j in range (cantidad_de_vehículos):
                                print("Ingrese el año del vehículo", marca, modelo, "número #", j + 1)
                                anio = input(">>")
                                print("Ingrese el cilindraje del vehículo", marca, modelo, "número #", j + 1)
                                cilindraje = input(">>")
                                print("Ingrese el precio del alquiler por día del vehículo", marca, modelo, "número #", j + 1)
                                precio_de_alquiler = input(">>")
                                print("Ingrese el precio del vehículo", marca, modelo, "número #", j + 1)
                                precio = input(">>")
                                print("Ingrese la placa del vehículo", marca, modelo, "número #", j + 1)
                                placa = input(">>")

                                #Guarda en la matriz los datos del vehículo
                                vehiculos.append([marca,modelo,anio,cilindraje,precio_de_alquiler,precio,placa,inhabilitado])


                            #Determina si se continúa en el ciclo
                            print("¿Desea seguir ingresando vehículos? si/no")
                            i = input(">>")
                            if(i == "no" or i == "No" or i == "NO"):
                                print("Usted regresará al menú\n")
                            elif(i == "si" or i == "Si" or i == "SI"):
                                print("Ingrese un nuevo Vehículo")
                            else:
                                print("Ingrese un valor correcto")
                                i = "si"

                        #Fin del ciclo

                        
                    else:
                        print("Usuario o conraseña incorrectos")

                elif opciones == 2:
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

                opciones = int(input("Desea gestionar el inventario (1) o desea salir (2)?"))
                if opciones == 1:
                    #inventario pendiente
                    print("Disculpe, pero el inventario está en mantenimiento...")

                elif opciones == 2:
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
        print(" ")
        print("Al iniciar como usuario no va a poder tener los mismos privilegios que si tienen")
        print("Los usuarios registrados")
        print(" ")

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

            opciones = int(input("Desea gestionar el inventario (1) o desea salir (2)?"))
            if opciones == 1:
                #inventario pendiente
                print("Disculpe, pero el inventario está en mantenimiento...")

            elif opciones == 2:
                salir = str(input("Si desea salir digite ´si´, en el caso contrario digite ´no´"))

                if salir == "si" or salir == "SI" or salir == "Si" or salir == "sI":

                    print("Adios, gracias por su visita!")

                    break
                    

                elif salir == "no" or salir == "NO" or salir == "No" or salir == "nO":

                    print("Como desee")

                
        elif cambio == "no" or cambio == "No" or cambio == "NO":
            
            print("Su ingreso ha sido exitoso")
            
       
    else:
        print("El valor ingresado no pertenece a un opcion")
        break
