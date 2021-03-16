salir=0
archivo = open("Ejercicio 9.csv","a")

while salir==0:
    
    print('\n----Lista de numero mayor a menor---')
    print('Iniciar programa (1)')
    print('salir (2)')
    opcion=int(input('ingrese una opcion: '))
    numeros=[]
    if opcion==1:
        a=int(input('Ingrese el primer numero: '))
        b=int(input('Ingrese el segundo numero: '))
        if a>b:
            for i in range(a,b-1,-1):
                print(i)
                numeros.append(i)
            archivo.write('Los numeros en orden descendente son:'+str(numeros)+'\n')

        else:
            for i in range(b,a-1,-1):
                print(i)
                numeros.append(i)
            archivo.write('Los numeros en orden descendente son:'+str(numeros)+'\n')



    if opcion==2:
        archivo.close()
        salir=1