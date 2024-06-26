opciones = 0
salir = 0
nomusu1 = 0

#Base de vehículos
vehiculos = []
reservas = []

horarios = [['San Jose', '0', '24'], ['Alajuela', '0', '24'], ['Guanacaste', '4', '23'], ['Limon', '6', '22'], ['Puntarenas', '5', '22'], ['Perez Zeledon', '7', '22']]

#Funcion para subir reservas

def subirReservas(): #Sube las reservas al archivo Reservas.txt
    global reservas
    archivo = open("Reservas.txt", "w")
    archivo.write(str(reservas))
    archivo.close()

def guardarReservas(): #Guarda las reservas en la variable global
    global reservas
    archivo = open("Reservas.txt", "r")
    todo = archivo.read()
    todo = eval(todo) #A falta de un metodo mejor, use Eval
    reservas = todo
    archivo.close()

guardarReservas()
subirReservas()

#Función para leer los vehiculos de la base de datos
def leer_vehiculos(vehiculos):

    #Variables para guardar los datos
    marca = "indefinido"
    anio = 0
    modelo = "indefinido"
    cilindraje = 0
    precio_de_alquiler = 0
    precio = 0
    placa = "indefinido"
    inhabilitado = False
    sede = "indefinido"

    #Carga el archivo en una variable para leer
    file = open("Vehiculos.txt","r")
    
    #Recorre el archivo
    for linea in file: #ALLAN CAMBIO DE :OPEN A ESTO
        if(linea != "\n"): #Verifica que la línea no esté vacía

            entrada2 = linea.strip("\n")#Elimina el enter

            entrada_dividida = entrada2.split(",")#Subdivide en un vector el vehículo

            marca = entrada_dividida[0]
            modelo = entrada_dividida[1]
            anio = entrada_dividida[2]
            cilindraje = entrada_dividida[3]
            precio_de_alquiler = entrada_dividida[4]
            precio = entrada_dividida[5]
            placa = entrada_dividida[6]
            if(entrada_dividida[7] == "True"):
                inhabilitado = True
            else:
                inhabilitado = False
            sede = entrada_dividida[8]
            vehiculos.append([marca,modelo,anio,cilindraje,precio_de_alquiler,precio,placa,inhabilitado,sede])
    file.close()

#Función para guardar los vehiculos en la base de datos
def escribir_vehiculos(vehiculos):
    #Carga el archivo en una variable para escribir
    file = open("Vehiculos.txt","w")

    #Recorre la matriz para escribir en la base de datos cada vehículo, con cada dato
    for vehiculo in vehiculos:
        file.write(vehiculo[0])
        file.write(",")
        file.write(vehiculo[1])
        file.write(",")
        file.write(vehiculo[2])
        file.write(",")
        file.write(vehiculo[3])
        file.write(",")
        file.write(vehiculo[4])
        file.write(",")
        file.write(vehiculo[5])
        file.write(",")
        file.write(vehiculo[6])
        file.write(",")
        if(vehiculo[7] == True):
            file.write("True")
        else:
            file.write("False")
        file.write(",")
        file.write(vehiculo[8])
        file.write("\n")
    file.close()

def listaModelo(marca, sede): #Devuelve los modelos disponibles de la marca dependiendo de su sede
    lista2 = []
    lista3 = []
    marca = str(marca)
    print(marca)
    for i in vehiculos: #Crea una lista con todos los vehiculos de la marca y sede elegidas
        if i[0].upper() == marca.upper() and i[8].upper() == sede.upper():
            lista2 += [i]
    cont = 0
    cont2 = 0
    for i in lista2: #Cuenta la cantidad de vehiculos disponibles de cada modelo
        x = i[1]
        for j in lista2:
            if x == j[1]:
                if j[7] == False:
                    cont2 +=1


        if [marca ,x, cont2] not in lista3: #Guarda la marca, su modelo y la cantidad Ej: ["Toyota", "Modelo 33", 2]
            lista3 += [[marca, x, cont2]]
            
        cont2 = 0
    estado = ""
    for i in lista3: #Si la cantidad es 0 entonces imprime que no esta disponible
        if i[2]==0:
            estado = "No Disponible"
        else:
            estado = i[2] # Imprime la marca, el modelo y su cantidad en caso de que haya al menos uno disponible
        print("    ",i[0],i[1],": ", estado)
    if lista2 == []:
        print("No disponible en la region")
        return False
    return True

def marcas(): #Crea una lista de cada marca en los vehiculos
    lista = []
    for i in vehiculos:
        if i[0] not in lista:
            lista += [i[0]]
    return lista
        
def reservar(marca, sede, ced): #Sirve para reservar un vehiculo, E: marca str, sede str, cedula str
    global reservas, vehiculos
    salir = False
    while salir == False: #Lo repite hasta que salir deje de ser False
        print()
        model = input("Escriba el modelo: ")
        print()
        x = False
        find = False
        for i in vehiculos: # Busca que el vehiculo sea el que se pidio comprobando la marca el modelo la sede y que este disponible
            if i[0] == marca and i[1]== model and i[7] == False and find == False and sede == i[8].upper():
                print("Disponible")
                veh = i
                x = True
                find = True
        if x == False: #Si
            x = "Disculpe " + model + " no disponible"
            print("Regresando al menu principal")
            print()
            salir = True
        if x == True:
            print()
            print("Para reservar necesitamos que nos indique un dia y hora de entrega", sede)
            print()
            print("Escriba la hora de entre las 0 a 24, indique con un numero entero en caso de que sea")
            print("en punto en otro caso, indicar minutos con numero con decimal. (Ej: 1.30)")
            hora = input("Hora: ")
            print()
            dia= input("Indique la cantidad de dias que desea reservar el vehiculo: ")
            print()
            carro = []
            for i in horarios:
                if i[0].upper() == sede:
                    print("Sede correcta")
                    if float(hora)>int(i[1]) and float(hora)<int(i[2]):
                        print("Horario Disponible!")

                        priceA = ''
                        for i in vehiculos:
                            if i[1]==model and priceA == '':
                                priceA = int(i[4])
                                priceV = int(i[5])
                        seguro = priceV * 0.045 + 10
                        priceR = priceA * int(dia) + seguro
                        
                        
                        for i in reservas:
                            if i[0]==ced:
                                print()
                                print("Su dinero es: ", i[3])
                                print("El monto para reservar es de : ", priceR)
                                print()
                                print("Desea realizar la reserva?")
                                des = input("Si o No: ")
                                if des.upper() == "SI":
                                    if int(i[3])-priceR < 0:
                                        print("No se puede realizar la reserva")
                                        salir = True

                                    else:
                                        print()
                                        print("Este es el monto restante de su cuenta: ", int(i[3])-priceR)
                                        print()
                                        i[3] = int(i[3])-priceR
                                        i[4] += [veh]
                                        print("Vehiculo reservado: ", veh[0], veh[1], veh[8])
                                        subirReservas()
                                        guardarReservas()
                                        
                                        
                                        
                                        for i in vehiculos:
                                            if i == veh:
                                                i[7] = True
                                        
                                        salir = True

                                elif des.upper() == "NO":
                                    salir = True

                                
                        
                    else:
                        print("Disculpe, la hora especificada de ", dia,"|", hora," no es permitida en la sede ", i[0],)
                        print("estos son los horarios: ")
                        print()
                        print("Sede San Jose: 00:00-23:59")
                        print("Sede Alajuela: 00:00-23:59")
                        print("Sede Guanacaste: 04:00-23:00")
                        print("Sede Limon: 06:00-22:00")
                        print("Sede Puntarenas:  05:00-22:00")
                        print("Sede Perez Zeledon: 07:00-22:00")

                
        else:
            print(x)
        escribir_vehiculos(vehiculos)
                                        
        vehiculos = []
                                        
        leer_vehiculos(vehiculos)



def verReservas():
    print()
    crear = True
    while crear == True:
        print()
        ced = input("Digite su cedula: " )
        lista = []
        cont = 0
        global reservas
        for i in reservas:
            lista += [i[0]]
            if i == ced:
                x = cont
            cont += 1
        if ced not in lista:
            usu = input("Digite su usuario: ")
            num = input("Digite su numero: ")
            din = input("Digite su dinero: ")
            reserva = [ced,usu,num,din,[]]
            reservas += [reserva]
            subirReservas()
            guardarReservas()
        else:
            print()
            print("Bienvenido a Reservar")
            print()
            validar = True
            while validar:
                res = input("Revisar Listado de vehiculos (1) o revisar vehiculos reservados  (2): ")   
                if res != '1' and res!= '2':
                    print("Respuesta Invalida")
                elif res == '1':
                    print()
                    cont= 0
                    listaMarcas = []
                    listar_vehiculos(vehiculos)
                    for i in marcas():
                        print(i, "(",cont,")")
                        listaMarcas += [[i, cont]]
                        cont += 1
                    print()
                    elegir = int(input("Elija la marca (numero): "))
                    cont = 0
                    for i in listaMarcas:
                        if i[1] == elegir:
                            elegir = i[0]
                    print()
                    print("Sede San Jose: 00:00-23:59")
                    print("Sede Alajuela: 00:00-23:59")
                    print("Sede Guanacaste: 04:00-23:00")
                    print("Sede Limon: 06:00-22:00")
                    print("Sede Puntarenas:  05:00-22:00")
                    print("Sede Perez Zeledon: 07:00-22:00")
                    print()
                    sal = False
                    while sal == False:
                        sed = input("Digite el nombre de su sede (sin tildes): ")
                        for i in horarios:
                            if sed.upper() == i[0].upper():
                                sal = True
                                break
                        if sal == False:
                            print("sede no disponible")
                    sed = sed.upper()
                    print()
                    if listaModelo(elegir, sed):
                        reservar(elegir, sed, ced)
                        validar = False
                        crear = False

                elif res == '2':
                    print()
                    print("Tus Vehiculos Reservados: ")
                    for i in reservas:
                        if i[0] == ced:
                            for j in i[4]:
                                print("Marca: ", j[0],
                                      "Modelo: ", j[1],
                                      "Año: ", j[2],
                                      "Cilindraje: ", j[3],
                                      "Precio Alquiler x dia: ", j[4],
                                      "Precio: ", j[5],
                                      "Placa: ", j[6],
                                      "Sede: ", j[8])
                    print()
                    validar = False
                    crear = False
                    break

    return

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
                    inventario_sedes("San Jose")
                elif(op == "2"):
                    verReservas()
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
                    verReservas()
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
                    verReservas()
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
                    inventario_sedes("Limon")
                elif(op == "2"):
                    verReservas()
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
                    verReservas()
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
                    verReservas()
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
                        sede = "San Jose"
                        valido = "si"
                    elif(sede == "2"):
                        sede = "Alajuela"
                        valido = "si"
                    elif(sede == "3"):
                        sede = "Guanacaste"
                        valido = "si"
                    elif(sede == "4"):
                        sede = "Limon"
                        valido = "si"
                    elif(sede == "5"):
                        sede = "Puntarenas"
                        valido = "si"
                    elif(sede == "6"):
                        sede = "Perez Zeledon"
                        valido = "si"
                    else:
                        print("Ingrese un valor valido")
                        valido == "no"

                # Guarda en la matriz los datos del vehículo
                vehiculos.append([marca,modelo,anio,cilindraje,precio_de_alquiler,precio,placa,inhabilitado,sede])

            # Determina si se continúa en el ciclo
            print("¿Desea seguir ingresando vehiculos? si/no")
            i = input(">>")
            if(i == "no" or i == "No" or i == "NO"):
                print("Usted regresará al menú\n")
            elif(i == "si" or i == "Si" or i == "SI"):
                print("Ingrese un nuevo vehículo")
            else:
                print("Ingrese un valor correcto")
                i = "si"
    else:
        print("\nIngrese el usuario y contraseña correctos\n")

#Carga la base de datos
leer_vehiculos(vehiculos)

#Ingresa al ciclo del menú
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

                    opciones = int(input("Desea gestionar el inventario (1) ver los vehiculos disponibles(2) ingresar sede(3) reservar(4) o salir (5)?"))
                if opciones == 1:
                    #Gestion Inventarios
                    gestion_inventario(vehiculos)
                    #Carga a la base de datos
                    escribir_vehiculos(vehiculos)
                    
                elif opciones== 2:
                    #Visualizar vehiculos
                    listar_vehiculos(vehiculos)

                elif opciones== 3:
                    #Invoca la función de sedes
                    sedes()

                elif opciones== 4:
                    #reservas
                    verReservas()
                    
                elif opciones == 5:
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

                opciones = int(input("Desea gestionar el inventario (1) ver los vehiculos disponibles(2) ingresar sede(3) reservar(4) o salir(5)?"))
                if opciones == 1:
                    gestion_inventario(vehiculos)
                    #Carga a la base de datos
                    escribir_vehiculos(vehiculos)




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

                elif opciones== 4:
                    #reservar
                    verReservas()

                elif opciones == 5:
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

            opciones = int(input("Desea gestionar el inventario (1) Ver los vehiculos disponibles(2) resesrvar(3) o salir(4)?"))
            if opciones == 1:
                #Gestion Inventarios
                gestion_inventario(vehiculos)
                #Carga a la base de datos
                escribir_vehiculos(vehiculos)
                
            elif opciones == 2:
                #Visualizar vehiculos
                listar_vehiculos(vehiculos)

            elif opciones== 3:
                #reservar
                verReservas()

                
            elif opciones == 4:
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
        #Carga a la base de datos
        escribir_vehiculos(vehiculos)
        
    elif inises == "5":
        #Visualizar vehiculos
        listar_vehiculos(vehiculos)
          
    else:
        print("El valor ingresado no pertenece a un opcion")
        break
