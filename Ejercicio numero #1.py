grupo1 = [[], []]
grupo2 = [[], []]
grupo3 = [[], []]

while True:
    print("Bienvenido a el sistema de ingreso de notas de U Fidelitas, seleccione el grupo a trabajar?")
    print("grupo 1(1), grupo 2(2), grupo 3(3)")
    seleccion=int(input(""))
    
    if seleccion==1:
        quedados=0
        aprobados=0
        notamayor=0
        notamenor=100
        for i in range(5):
            nombre=input("Cual es el nombre del estudiante?")
            grupo1[0].append(nombre)
            nota=int(input("Cual fue la nota final del estudiante?"))
            grupo1[1].append(nota)

            if nota>=70:
                aprobados+=1
            elif nota < 70:
                quedados+=1
            
            if nota > notamayor:
                notamayor = nota
                estudiante_nota_mas_alta = nombre

      
            if nota < notamenor:
                notamenor = nota
                estudiante_nota_menor = nombre

            porcentaje_aprobados=(aprobados/5)*100
                
         
            notas=grupo1[1]
            total=sum(notas)
            promedio=total/5
        
        
        print(f"El promedio del grupo fue de: {promedio:}")
        print(f"En total, {aprobados} estudiantes pasaron el curso y {quedados} estudiantes se quedaron.")
        print(f"el porcentaje de estudiantes aprobados fue de el: {porcentaje_aprobados}%")
        print(f"La nota mas alta fue de {notamayor} pertenece a {estudiante_nota_mas_alta }y la nota mas baja fue de {notamenor} y pertenece a {estudiante_nota_menor }")


            

    elif seleccion==2:
        quedados=0
        aprobados=0
        notamayor=0
        notamenor=100
        for i in range(5):
            nombre=input("Cual es el nombre del estudiante?")
            grupo2[0].append(nombre)
            nota=int(input("Cual fue la nota final del estudiante?"))
            grupo2[1].append(nota)

            if nota>=70:
                aprobados+=1
            elif nota < 70:
                quedados+=1
            
            if nota > notamayor:
                notamayor = nota
                estudiante_nota_mas_alta = nombre

      
            if nota < notamenor:
                notamenor = nota
                estudiante_nota_menor = nombre
            porcentaje_aprobados=(aprobados/5)*100
                
         
            notas=grupo2[1]
            total=sum(notas)
            promedio=total/5
        
        
        print(f"El promedio del grupo fue de: {promedio:}")
        print(f"En total, {aprobados} estudiantes pasaron el curso y {quedados} estudiantes se quedaron.")
        print(f"el porcentaje de estudiantes aprobados fue de el: {porcentaje_aprobados}%")
        print(f"La nota mas alta fue de {notamayor} pertenece a {estudiante_nota_mas_alta }y la nota mas baja fue de {notamenor} y pertenece a {estudiante_nota_menor }")

    elif seleccion==3:
        quedados=0
        aprobados=0
        notamayor=0
        notamenor=100
        for i in range(5):
            nombre=input("Cual es el nombre del estudiante?")
            grupo3[0].append(nombre)
            nota=int(input("Cual fue la nota final del estudiante?"))
            grupo3[1].append(nota)

            if nota>=70:
                aprobados+=1
            elif nota < 70:
                quedados+=1
            
            if nota > notamayor:
                notamayor = nota
                estudiante_nota_mas_alta = nombre

      
            if nota < notamenor:
                notamenor = nota
                estudiante_nota_menor = nombre
            porcentaje_aprobados=(aprobados/5)*100
                
         
            notas=grupo3[1]
            total=sum(notas)
            promedio=total/5
        
        
        print(f"El promedio del grupo fue de: {promedio:}")
        print(f"En total, {aprobados} estudiantes pasaron el curso y {quedados} estudiantes se quedaron.")
        print(f"el porcentaje de estudiantes aprobados fue de el: {porcentaje_aprobados}%")
        print(f"La nota mas alta fue de {notamayor} pertenece a {estudiante_nota_mas_alta }y la nota mas baja fue de {notamenor} y pertenece a {estudiante_nota_menor }")S
        
