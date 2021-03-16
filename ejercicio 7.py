salir=0
archivo = open("Ejercicio 7.csv","a")

while salir==0:
    
    print('\n----Factorial de multilos de 7---')
    print('Iniciar programa (1)')
    print('salir (2)')
    opcion=int(input('ingrese una opcion: '))
    
    if opcion==1:
        c=1
        num=int(input('ingrese un numero divisible dentro de 7 para calcuar el factorial:'))
        b=num%7
        if b==0:
            for i in range(1,num+1,1):
                c=c*i
            print('El factorial de '+str(num)+'es: '+str(c))
            archivo.write('el factorial de '+str(num)+'es: '+str(c)+'\n')

        else:
            print('Error: debe ingresr un numero multiplo de 7')
            
    if opcion==2:
        archivo.close()
        salir=1