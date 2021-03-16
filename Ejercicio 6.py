salir=0
archivo = open("Ejercicio 6.csv","a")

while salir==0:
    numeros=[]
    print('\n----Determinar tipo de triangulo---')
    print('Iniciar programa (1)')
    print('salir (2)')
    opcion=int(input('ingrese una opcion: '))
    
    if opcion==1:
        a=int(input('Ingrese la medida del lado A: '))
        b=int(input('Ingrese la medida del lado b: '))
        c=int(input('Ingrese la medida del lado c: '))
        
        if a==b==c:
            print('Es un triangulo equilatero')
            archivo.write('las medidas a='+str(a)+', b='+str(b)+', c='+str(c)+' coresponden aun triangulo equilatero \n')
        if a==b!=c or a==c!=b or b==c!=a:
            print( 'Es un tiangulo Isoceles')
            archivo.write('las medidas a='+str(a)+', b='+str(b)+', c='+str(c)+' coresponden aun triangulo isoceles \n')
        if a!=b!=c:
            print('Esun triangulo escaleno')
            archivo.write('las medidas a='+str(a)+', b='+str(b)+', c='+str(c)+' coresponden aun triangulo escaleno \n')

    if opcion==2:
        archivo.close()
        salir=1