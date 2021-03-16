import psycopg2
from os import system

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



archivo = open("Calculadora.csv","a")
num=1
system("cls")
while num==1:
    
    print ("-----------------Calculadora----------- ")
    print ("suma............(s)")
    print ("Resta...........(r)")
    print ("Multiplicacion..(m)")
    print ("division........(d)")
    print ("salir...........(z)")
    
    operacion=input("Indique la operacion que desea realizar:")
    
    if operacion.isdigit():
        print ("ingrese solamente la letra correspondiente")
    elif operacion.isalnum: 
        if operacion =="s": 
            system("cls")
            print ("operacion seleccionada fue Suma")
            x=float(input("Ingrese el primer numero:"))
            y=float(input("Ingrese el segundo numero:"))
            z=x+y
            archivo.write("suma;"+str(z)+'\n')
	        
            insertar_datos ('suma',str(z))
            print("el resultado de la suma es",z)
            
        if operacion =="r": 
            system("cls")
            print ("operacion seleccionada fue Resta")
            x=float(input("Ingrese el minuendo:"))
            y=float(input("Ingrese el sustraendo:"))
            z=x-y
            print("el resultado de la resta es:",z)
        if operacion =="m": 
            system("cls")
            print ("operacion seleccionada fue Multiplicacion")
            x=float(input("Ingrese el primer numero:"))
            y=float(input("ingrese el segunod numero:"))
            z=x*y
            print("el resultado de la multiplicacion es:",z)
        if operacion =="d": 
            system("cls")
            print ("operacion seleccionada fue Division")
            x=float(input("Ingrese el dividendo:"))
            y=float(input("ingrese el divisor:"))
            if y==0: 
                print("error el divisor no puede ser cero")
                y=float(input("ingrese el divisor:"))
            elif y!=0:
                z=x/y
                print("el resultado de la division es:",z)
        if operacion =="z":
            system("cls")
            archivo.close()

            num=0