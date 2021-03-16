salir=0
archivo = open("Ejercicio 8.csv","a")
numeros=[]
while salir==0:
    
    print('\n----Numeros de inicio y fin---')
    print('Iniciar programa (1)')
    print('salir (2)')
    opcion=int(input('ingrese una opcion: '))
    
    if opcion==1:
        numinicio=int(input('Ingrese el numero de inicio: '))
        numfin=int(input('ingrese el numero final:'))
        for i in range(numinicio,numfin+1,1):
            print(i)
            numeros.append(i)
        archivo.write('Los numeros son:'+str(numeros)+'\n')

    if opcion==2:
        archivo.close()
        salir=1