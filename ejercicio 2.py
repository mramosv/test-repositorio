salir=0
archivo = open("Ejercicio 2.csv","a")


while salir==0:

    print('\n----Divisores----')
    print('Iniciar programa (1)')
    print('salir (2)')
    opcion=int(input('ingrese una opcion: '))
    i=1
    if opcion==1:

        num=int(input("numero:"))
        print('los divisores de '+ str(num) +' son:')
        archivo.write("los divisores de: "+str(num)+' son: \n')
        for i in range(1,num+1,1):
            if (num%i)==0:
                print(i)
                archivo.write(str(i)+'\n')

    if opcion==2:
        archivo.close()
        salir=1