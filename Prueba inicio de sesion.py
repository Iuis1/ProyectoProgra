
print("Este es un sistema de prueba de un inicio de seision utilizando unicamente variables")

while True:

    inises=input("Bienvenido desea, crear un usuario(1) o iniciar sesion(2)")


    if inises=="1":
        nomusu1=str(input("Ingrese el nombre de usuario que desea utilizar:"))
        contra1=str(input("Ingrese la contrasena que desea utilizar:"))
        deseoini=str(input("Usuario registrado con exito, desea iniciar sesion(si)(no)?"))

        if deseoini=="si":
            inicio_sesion_usu1=str(input("Ingrese su nombre de usuario: "))

            if inicio_sesion_usu1==nomusu1:
                inicio_sesion_contra1=str(input("Ingrese su contrasena:"))
                
                if inicio_sesion_contra1==contra1:
                    print("Inicio de sesion exitoso")
                    
                elif inicio_sesion_contra1 != contra1:
                    print("La contrasena ingresada no es valida")
                    
            elif inicio_sesion_usu1 != nomusu1:
                print("El usuario ingresado no esta registrado")
                
            elif deseoini=="no":
                break


    elif inises=="2":
        
        inises_nomusu1=str(input("Ingrese su usuario: "))
        if inises_nomusu1!=nomusu1:
            print("El nombre de usuario no esta registrado")
        elif inises_nomusu1==inicio_sesion_usu1:
            inises_contra1=str(input("Ingrese su contrasena: "))
            if inises_contra1==contra1:
                print("Inicio de sesion exitoso")


        else:
            print("No existe ningun usuario registrado")

    else:
        print("El valor ingresado no pertenece a un opcion")
        break
