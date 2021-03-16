import psycopg2
from os import system
#constantes globales
PSQL_HOST = "localhost"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = "ssd21"
PSQL_DB   = "Calculadora"
calculo=4
resultado=3
#conexion
direccion_conexion= """host=%s port=%s user=%s password=%s dbname=%s"""% (PSQL_HOST,PSQL_PORT,PSQL_USER,PSQL_PASS,PSQL_DB)
conexion = psycopg2.connect(direccion_conexion)
cursor=conexion.cursor()
#qwery

cursor.execute("""INSERT INTO public."Historial"("Calculo","Resultado")VALUES(%s,%s)""",(calculo,resultado))
conexion.commit()


SQL='SELECT * FROM public."Historial"'
cursor.execute(SQL)
#obtener valores de la base de datos creada previamente
valores=cursor.fetchall()
cursor.close()
conexion.close()
print('valores de la tabla: ', valores)
