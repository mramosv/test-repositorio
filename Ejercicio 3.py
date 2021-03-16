salir=0
archivo = open("Ejercicio 3.csv","a")

while salir==0:

    print('\n----Conteo de vocales en palabras----')
    print('Iniciar programa (1)')
    print('salir (2)')
    opcion=int(input('ingrese una opcion: '))
    
    if opcion==1:
        a=0
        conteo=0
        palabra=input("Ingrese una palabra: ")
        while a<len(palabra):
            b=palabra[a]
            if b=='a':
                conteo=conteo+1
            if b=='e':
                conteo=conteo+1
            if b=='i':
                conteo=conteo+1
            if b=='o':
                conteo=conteo+1
            if b=='u':
                conteo=conteo+1
            a=a+1
        print("la palabra tiene: "+str(conteo)+ " vocales")
        archivo.write("La palabra "+str(palabra)+ " tiene "+str(conteo)+' Vocales \n')


    if opcion==2:
        archivo.close()
        salir=1