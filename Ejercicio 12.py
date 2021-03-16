salir=0
archivo = open("Ejercicio 12.csv","a")

while salir==0:

    print('\n----Notas----')
    print('Iniciar programa (1)')
    print('salir (2)')
    opcion=int(input('ingrese una opcion: '))
    
    if opcion==1:
        nota1=int(input('Ingrese la primera nota: '))
        nota2=int(input('Ingrese la segunda nota: '))
        nota3=int(input('Ingrese la tercera nota: '))

        if (0<=nota1<101) and (0<=nota2<101) and (0<=nota3<101): 
            promedio=((nota1+nota2+nota3)/3)

            if promedio>60:
                print('promedio:'+str(promedio))
                print('Aprobado')
                archivo.write('El promedio de las notas es:'+str(promedio)+' y el alumno esta aprobado\n')
            else:
                print('promedio:'+str(promedio))
                print('Reprobado')
                archivo.write('El promedio de las notas es:'+str(promedio)+' y el alumno esta reprobado\n')
        else:
            print('ingrese notas validas')
    if opcion==2:
        archivo.close()
        salir=1