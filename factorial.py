from re import A
import psycopg2
from os import system

system("cls")
a=1
salir=1
PSQL_HOST = "localhost"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = "ssd21"
PSQL_DB   = "Calculadora"

def insertar_datos (Calculo,Resultado):
    
    try:
        conexion = psycopg2.connect(user = "postgres",password = "ssd21", host = "localhost", port = "5432",database = "postgres")

        cursor=conexion.cursor()
        cursor.execute("""INSERT INTO public."Historial de calculos"(Calculo,Resultado) VALUES(%s,%s)""",(Calculo,Resultado))
        conexion.commit()
        conexion.close()
    
    except (Exception, psycopg2.Error) as error :
	    print(error)
	    print("Conexcion fallida, intente de nuevo")

archivo = open("factorial.csv","a")

while salir==1:

    try:
        caracter=input("ingrese el numero a calcular el factorial:")
        if caracter=='z':
            archivo.close()
            salir=0
        else:
            ingreso=int(caracter)
            i=1
            if ingreso<1:
                print("ingrese u numero valido mayor a 1")
            if ingreso==0:
                a=1
            if ingreso>0:
                for i in range (ingreso,0,-1):
                    a=a*i   
                    i=i+1
                print ("el factorial es: " +str(a))
                archivo.write("Factorial de "+str(ingreso)+" es: "+str(a)+'\n')
                #insertar_datos ('Factorial: ',str(a))
                a=1
            
    except:
        print("error unicamente ingrese numeros o z para salir")        
    