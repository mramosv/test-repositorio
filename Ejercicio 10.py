salir=0
archivo = open("Ejercicio 10.csv","a")

while salir==0:

    print('\n----Numero de cada vocal en una palabra----')
    print('Iniciar programa (1)')
    print('salir (2)')
    opcion=int(input('ingrese una opcion: '))
    
    if opcion==1:
        z=0
        a=0
        e=0
        i=0
        o=0
        u=0
        palabra=input("Ingrese una palabra: ")
        while z<len(palabra):
            b=palabra[z]
            if b=='a':
                a=a+1
            if b=='e':
                e=e+1
            if b=='i':
                i=i+1
            if b=='o':
                o=0+1
            if b=='u':
                u=u+1
            z=z+1
        print('Resultado:')
        print('A= '+str(a))
        print('E= '+str(e))
        print('I= '+str(i))
        print('O= '+str(o))
        print('U= '+str(u))
        archivo.write('\n Resultado de la palabra: '+str(palabra)+  '\n')
        archivo.write('A= '+str(a)+'\n')
        archivo.write('E= '+str(e)+'\n')
        archivo.write('I= '+str(i)+'\n')
        archivo.write('O= '+str(o)+'\n')
        archivo.write('U= '+str(u)+'\n')


    if opcion==2:
        archivo.close()
        salir=1