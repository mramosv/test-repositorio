import psycopg2
from os import system

PSQL_HOST = "localhost"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = "ssd21"
PSQL_DB   = "Tareaparcial"

#conexion

def insertar_datos(num1,num2,num3,resultado):
    try:
        direccion_conexion= """host=%s port=%s user=%s password=%s dbname=%s"""% (PSQL_HOST,PSQL_PORT,PSQL_USER,PSQL_PASS,PSQL_DB)
        conexion = psycopg2.connect(direccion_conexion)
        cursor=conexion.cursor()
        cursor.execute("""INSERT INTO public.e1(num1, num2, num3, resultado)VALUES(%s,%s,%s,%s);""",(primernumero,segundonumero,tercernumero,suma))
        conexion.commit()
        conexion.close()
    except(exception,psycopg2.Error) as error:
        print(error)
        print('fallo')
        
salir=0
archivo = open("Ejercicio 1.csv","a")
system("cls")

while salir==0:

    try:

        print('\niniciar programa (1)')
        print('salir (2)')
        print('consultar historial(3)')
        opcion=int(input('ingrese una opcion: '))

        if opcion==1:

            primernumero=int(input("Ingrese el primer numero:"))
            segundonumero=int(input("Ingrese el segundo numero:"))
            tercernumero=int(input("Ingrese el tercer numero numero:"))


            if primernumero>segundonumero and primernumero>tercernumero:
                print('La suma de los tres numeros es:')
                suma=primernumero+segundonumero+tercernumero
                print(suma)
                archivo.write("La suma de los tres numeros es:: "+str(suma)+'\n')
                insertar_datos(primernumero,segundonumero,tercernumero,suma)
               

            if segundonumero>primernumero and segundonumero>tercernumero:
                print('La multiplicacion de los tres nuemeros es:')
                multiplicacion=primernumero*segundonumero*tercernumero
                print(multiplicacion)
                archivo.write("La multiplicacion de los tres numeros es:: "+str(multiplicacion)+'\n')


            if tercernumero>segundonumero and tercernumero>primernumero:
                print('La concatenacion de los nuemeros es:')
                a=str(primernumero)
                b=str(segundonumero)
                c=str(tercernumero)
                print(a+b+c)
                archivo.write("La concatenacion los tres numeros es:: "+str(a+b+c)+'\n')


            if primernumero==segundonumero!=tercernumero:
                print('El numero distinto es:')
                print(tercernumero)
                archivo.write("El numero distinto es: "+str(tercernumero)+'\n')


            if primernumero==tercernumero!=segundonumero:
                print('El numero distinto es:')
                print(segundonumero)
                archivo.write("El numero distinto es: "+str(segundonumero)+'\n')


            if segundonumero==tercernumero!=primernumero:
                print('El numero distinto es:')
                print(tercernumero)
                archivo.write("El numero distinto es: "+str(primernumero)+'\n')


            if primernumero==segundonumero ==tercernumero:
                print('Todos los numeros son iguales')
                archivo.write("Todos los numeros son iguales "+'\n')

        
        if opcion==2:
            archivo.close()
            
            salir=1
        if opcion==3:
            print('historial')
            direccion_conexion= """host=%s port=%s user=%s password=%s dbname=%s"""% (PSQL_HOST,PSQL_PORT,PSQL_USER,PSQL_PASS,PSQL_DB)
            conexion = psycopg2.connect(direccion_conexion)
            cursor=conexion.cursor()
            SQL='SELECT * FROM public.e1;'
            cursor.execute(SQL)
            valores=cursor.fetchall()
            print('valores de la tabla: ', valores)
            conexion.close()
        if opcion>3:
            print('\nIngrese una opcion Valida')


    except:
        print('\nIngrese una opcion valida')