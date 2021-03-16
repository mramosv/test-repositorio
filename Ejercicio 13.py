salir=0
archivo = open("Ejercicio 13.csv","a")

while salir==0:

    print('\n----Año visiesto----')
    print('Iniciar programa (1)')
    print('salir (2)')
    opcion=int(input('ingrese una opcion: '))
    
    if opcion==1:
        año=int(input('Ingrese al año: '))
        if año%4 ==0:
            if año%100==0:
                if año%400==0:
                    print('El año'+str(año)+'es un año bisiesto')
                    archivo.write('El año '+str(año)+' es un año bisiesto\n')
                else:
                    print ('el año '+str(año)+' no es visiesto')
                    archivo.write('El año '+str(año)+' NO es un año bisiesto\n')
            else:
                print ('el año '+str(año)+' no es visiesto')
                archivo.write('El año '+str(año)+' NO es un año bisiesto\n')

        else:
            print ('el año '+str(año)+' no es visiesto')
            archivo.write('El año '+str(año)+' No es un año bisiesto\n')


    if opcion==2:
        archivo.close()
        salir=1