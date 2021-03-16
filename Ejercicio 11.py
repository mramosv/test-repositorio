salir=0
archivo = open("Ejercicio 11.csv","a")

while salir==0:

    print('\n----Area de figuras geometricas----')
    print('Iniciar programa (1)')
    print('salir (2)')
    opcion=int(input('ingrese una opcion: '))
    
    if opcion==1:
        print('(1) Circulo')
        print('(2) Triangulo')
        print('(3) Cuadrado')
        print('(4) Rectangulo')
        figura=int(input('Seleccione una opcion: '))
        if figura==1:
            print('Circulo')
            radio=float(input('Ingrese el radio: '))
            if radio>0:
                acirculo=3.14159*(radio*radio)
                print('El area del circulo es:'+str(acirculo)+' m^2')
                archivo.write('El area del circulo es: '+str(acirculo)+' m^2 \n')
            else:
                print("Ingrese un radio mayor a 0")
        if figura==2:
            print('Triangulo')
            base=float(input('Ingrese la base: '))
            altura=float(input('Ingrese la altura: '))
            if base>0 and altura>0:
                atriangulo=0.5*(base*altura)
                print('El area del triangulo es: '+str(atriangulo)+' m^2')
                archivo.write('El area del triangulo es: '+str(atriangulo)+' m^2 \n')
            else:
                print("Ingrese valores mayores a 0")
        if figura==3:
            print('Cuadrado')
            lado=float(input('Ingrese el Lado: '))
            if lado>0:
                acuadrado=(lado*lado)
                print('El area del cuadrado es: '+str(acuadrado)+' m^2')
                archivo.write('El area del cuadrado es: '+str(acuadrado)+' m^2 \n')
            else:
                print("Ingrese un lado mayor a 0")
        if figura==4:
            print('Rectangulo')
            base=float(input('Ingrese la bse: '))
            altura=float(input('Ingrese la altura: '))
            
            if base>0 and altura>0:
                arectangulo=(base*altura)
                print('El area del rectangulo es: '+str(arectangulo)+' m^2')
                archivo.write('El area del rectangulo es: '+str(arectangulo)+' m^2 \n')
            else:
                print("Ingrese valores mayores 0")
        if figura>4:
            print('Selecione una opcion valida')

    if opcion==2:
        archivo.close()
        salir=1