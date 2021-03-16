salir=0
archivo = open("Ejercicio 4.csv","a")

while salir==0:

    print('\n----Suma de numeros----')
    print('Iniciar programa (1)')
    print('salir (2)')
    opcion=int(input('ingrese una opcion: '))
    acumulado=0
    if opcion==1:
        numero=int(input("Ingrese una nuemero: "))
        for i in range(1,numero+1,1):
            acumulado = acumulado+i
            
        print('La suma de numeros desde 0 hasta '+ str(numero)+' es: '+ str(acumulado))
        archivo.write('La suma de numeros desde 0 hasta '+ str(numero)+' es: '+ str(acumulado)+' \n')


    if opcion==2:
        archivo.close()
        salir=1