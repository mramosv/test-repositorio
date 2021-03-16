salir=0
archivo = open("Ejercicio 14.csv","a")

while salir==0:

    print('\n----Taxis----')
    print('Iniciar programa (1)')
    print('salir (2)')
    opcion=int(input('ingrese una opcion: '))
    
    if opcion==1:
        taxi=int(input('Ingrese al año del taxi: '))
        km=int(input('ingrese el kilometraje del taxi: '))
        
        if taxi<2007 and km>20000:
            print('Este taxi debe renovarse')
            archivo.write('El taxi año '+str(taxi)+'y km '+str(km)+' debe renovarse\n')
        else:
            if 2007<=taxi<=2013 and km>20000:
                print('Este taxi debe recibir mantenimiento')
                archivo.write('El taxi año '+str(taxi)+'y km '+str(km)+' debe recibir mantenimiento\n')
            else:
                if taxi>2013 and km<10000:
                    print('taxi en optimas condiciones')
                    archivo.write('El taxi año '+str(taxi)+'y km '+str(km)+' se encuentra en optimas condiciones\n')
                else:
                    print('Mecanico')
                    archivo.write('El taxi año '+str(taxi)+'y km '+str(km)+' debe llevarse al mecanico\n')


    if opcion==2:
        archivo.close()
        salir=1