
print("Este es un sistema de prueba de un inicio de seision utilizando unicamente variables")

nomusu1 = 0
inicio_sesion_usu1 = 0

while True:

    inises=input("Bienvenido desea, crear un usuario(1) o iniciar sesion(2) o ingresar como invitado (3)")
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

                
        elif cambio == "no" or cambio == "No" or cambio == "NO":
            
            print("Su ingreso ha sido exitoso")
            
       
    else:
        print("El valor ingresado no pertenece a un opcion")
        break
