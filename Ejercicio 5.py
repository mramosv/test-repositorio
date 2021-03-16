salir=0
archivo = open("Ejercicio 5.csv","a")

while salir==0:
    numeros=[]
    print('\n----Numeros impares de 0 a 100---')
    print('Iniciar programa (1)')
    print('salir (2)')
    opcion=int(input('ingrese una opcion: '))
    acumulado=0
    if opcion==1:
        conteo=0
        for i in range(1,100+1,1):
            if i%2==0:
                conteo=conteo+1
                numeros.append(i)
        print('De 0 a 100 hay: '+str(conteo)+' numeros impares, los cuales son:')
        print(numeros)
        archivo.write('De 0 a 100 hay: '+str(conteo)+' numeros impares, los cuales son:'+str(numeros)+' \n')

    if opcion==2:
        archivo.close()
        salir=1