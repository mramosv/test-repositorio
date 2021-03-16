from numpy import diag
import psycopg2
from os import system
from datetime import date
from datetime import datetime

PSQL_HOST = "localhost"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = "ssd21"
PSQL_DB   = "Parcial"

#conexion programa 1

def insertar_p1(mayor,menor):
    try:
        direccion_conexion= """host=%s port=%s user=%s password=%s dbname=%s"""% (PSQL_HOST,PSQL_PORT,PSQL_USER,PSQL_PASS,PSQL_DB)
        conexion = psycopg2.connect(direccion_conexion)
        cursor=conexion.cursor()
        cursor.execute("""INSERT INTO public.p1(mayor,menor)VALUES(%s,%s);""",(mayor,menor))
        conexion.commit()
        conexion.close()
    except(exception,psycopg2.Error) as error:
        print(error)
        print('fallo')

#conexion programa 2
def insertar_p2(horas,pago):
    try:
        direccion_conexion= """host=%s port=%s user=%s password=%s dbname=%s"""% (PSQL_HOST,PSQL_PORT,PSQL_USER,PSQL_PASS,PSQL_DB)
        conexion = psycopg2.connect(direccion_conexion)
        cursor=conexion.cursor()
        cursor.execute("""INSERT INTO public.p2(horas,pago)VALUES(%s,%s);""",(horas,pago))
        conexion.commit()
        conexion.close()
    except(exception,psycopg2.Error) as error:
        print(error)
        print('fallo')
#conexion programa 3
def insertar_p3(a,b,c,tipo):
    try:
        direccion_conexion= """host=%s port=%s user=%s password=%s dbname=%s"""% (PSQL_HOST,PSQL_PORT,PSQL_USER,PSQL_PASS,PSQL_DB)
        conexion = psycopg2.connect(direccion_conexion)
        cursor=conexion.cursor()
        cursor.execute("""INSERT INTO public.p3(a,b,c,tipo)VALUES(%s,%s,%s,%s);""",(a,b,c,tipo))
        conexion.commit()
        conexion.close()
    except(exception,psycopg2.Error) as error:
        print(error)
        print('fallo')
#conexion programa 4

def insertar_p4(año,mes,dia,edad):
    try:
        direccion_conexion= """host=%s port=%s user=%s password=%s dbname=%s"""% (PSQL_HOST,PSQL_PORT,PSQL_USER,PSQL_PASS,PSQL_DB)
        conexion = psycopg2.connect(direccion_conexion)
        cursor=conexion.cursor()
        cursor.execute("""INSERT INTO public.p4("año",mes,dia,edad)VALUES(%s,%s,%s,%s);""",(año,mes,dia,edad))
        conexion.commit()
        conexion.close()
    except(exception,psycopg2.Error) as error:
        print(error)
        print('fallo')




numeros=[]
salir=0
archivo = open("primerparcial.csv","a")
system("cls")

while salir==0:

    try:
        print('\n---Primer parcial---')
        print('(1) Numero mayor y menor')
        print('(2) Sueldo semanal')
        print('(3) Tipo de triangulo')
        print('(4) Edad al dia de hoy')
        print('(5) Salir')
        
        opcion=int(input('ingrese una opcion: '))

        if opcion==1:
            try:
                archivo = open("primerparcial.csv","a")
                lista=[]
                for x in range(5):
                    valor=int(input("Ingrese el valor de la posicion {} : ".format(x+1)))
                    lista.append(valor)
                lista.sort()
                print('\nEl valor mas alto es: '+str(lista[4]))
                print('El valor mas bajo es: '+str(lista[0]))
                archivo.write('\n\nPrograma mayor, menor\n')
                archivo.write("el numero mayor fue: "+str(lista[4])+" ; el numero menor fue: "+str(lista[0])+"\n")
                archivo.close()
                mayor=lista[4]
                menor=lista[0]
                insertar_p1(mayor,menor)
            except:
                print('Solo debe ingresar numeros')
       
        if opcion==2:
            try:
                archivo = open("primerparcial.csv","a")
                horas=int(input('\ncuantas horas trabajo la persona: '))
                if horas<=40:
                    pago=horas*50
                
                if horas>40:
                    pago=(2000)+((horas-40)*75)
                
                print('su sueldo sera: '+str(pago)+(' Q'))
                archivo.write('\n\nPrograma sueldo semanal\n')
                archivo.write("Por trabajar: "+str(horas)+" horas, su sueldo sera: "+str(pago)+" Q\n")
                archivo.close()
                insertar_p2(horas,pago)
            except:
                print('Solo debe ingresar numeros')
                
        if opcion==3:
            try:
                archivo = open("primerparcial.csv","a")
                a=int(input('\nIngrese la medida del lado A: '))
                b=int(input('Ingrese la medida del lado b: '))
                c=int(input('Ingrese la medida del lado c: '))
                if a==b==c:
                    print('\nEs un triangulo equilatero')
                    archivo.write('\n\nPrograma de triangulos\n')
                    archivo.write('las medidas a='+str(a)+', b='+str(b)+', c='+str(c)+' coresponden aun triangulo equilatero \n')
                    archivo.close()
                    tipo='Equilatero'
                    insertar_p3(a,b,c,tipo)
                    
                if a==b!=c or a==c!=b or b==c!=a:
                    print( '\nEs un tiangulo Isoceles')
                    archivo.write('\n\nPrograma de triangulos\n')
                    archivo.write('las medidas a='+str(a)+', b='+str(b)+', c='+str(c)+' coresponden aun triangulo isoceles \n')
                    archivo.close()
                    tipo='isoceles'
                    insertar_p3(a,b,c,tipo)

                if a!=b!=c:
                    print('\nEsun triangulo escaleno')
                    archivo.write('\n\nPrograma de triangulos\n')
                    archivo.write('las medidas a='+str(a)+', b='+str(b)+', c='+str(c)+' coresponden aun triangulo escaleno \n')
                    archivo.close()
                    tipo='Escaleno'
                    insertar_p3(a,b,c,tipo)

                if opcion==4:
                    print('\nIngrese una opcion Valida')
                
                archivo.close()
            except:
                print('Solo debe ingresar numeros')

        if opcion==4:    
            try:
                archivo = open("primerparcial.csv","a")
                day=int(input('\nIngrese el dia de nacimiento: '))
                month=int(input('Ingrese el mes de nacimeinto: '))
                year=int(input('Ingrese el año de nacimeinto: '))
                fecha_actual=date.today()
                resultado=fecha_actual.year-year
                resultado -= ((fecha_actual.month,fecha_actual.day)<(month,day))
                print('\nUsted tiene '+str(resultado)+' años')
                archivo.write('\n\nPrograma de la edad\n')
                archivo.write('Usted tiene: '+str(resultado)+' años\n')
                archivo.close()
                año=year
                mes=month
                dia=day
                edad=resultado
                insertar_p4(año,mes,dia,edad)


            except:
                print('Ingrese datos Validos')
            

        if opcion==5:
            salir=1
            archivo.close()
        

    except:
        print('\nIngrese una opcion valida')