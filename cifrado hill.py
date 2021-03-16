import numpy as np
from os import system
salir=0
system("cls")

while salir==0:
    try:
        print('\n----Cifrado Hill----')
        print('(1) Iniciar programa ')
        print('(2) salir ')
        opcion=int(input('ingrese una opcion: '))
    
    

        if opcion==1:

            #system("cls")
            filas=0
            x=(input("\nIngrese el texto a cifrar: ")) #x es el tecto ingresado
            #print(x)
            #print(len(x))
            a=0 # a es la  variable de conteo a igualar a la longitud x

            columnas=3
            filas=int(len(x)/3)
            residuo= int(len(x))%3
            if  residuo !=0:
                filas=filas+1
            d=0 #variable para recorriodo de columnas
            e=0 #variable control de filas
            #print(filas)
            matriz=np.zeros([filas,columnas])
            mult=np.zeros([filas,columnas])
            matriz2=np.zeros([filas,columnas])

            while a < len(x):
                
                b=x[a] #b muestra datos de la matriz original
                if b =="a":
                    c=0 #c es variable de mi segunda matriz
                if b =="b":
                    c=1
                if b =="c":
                    c=2
                if b =="d":
                    c=3
                if b =="e":
                    c=4
                if b =="f":
                    c=5
                if b =="g":
                    c=6
                if b =="h":
                    c=7
                if b =="i":
                    c=8
                if b =="j":
                    c=9
                if b =="k":
                    c=10
                if b =="l":
                    c=11
                if b =="m":
                    c=12
                if b =="n":
                    c=13
                if b =="ñ":
                    c=14
                if b =="o":
                    c=15
                if b =="p":
                    c=16
                if b =="q":
                    c=17
                if b =="r":
                    c=18
                if b =="s":
                    c=19
                if b =="t":
                    c=20
                if b =="u":
                    c=21
                if b =="v":
                    c=22
                if b =="w":
                    c=23
                if b =="x":
                    c=24
                if b =="y":
                    c=25
                if b =="z":
                    c=26
                if b ==" ":
                    c=27
                if b ==".":
                    c=28
                if b ==",":
                    c=29
                if d>2:
                    d=0
                    e=e+1
                if e>filas:
                    e=0
                matriz[e,d]=c

                #print(b)
                #print(c)
                a=a+1
                d=d+1
                
            llave=np.array([[1,2,3],[0,4,5],[1,0,6]])
            mensaje=[]
            #grupo1=np.array([2,21,0])
            #print(matriz)
           #print("Texto cifrado:")
            i=0

            for i in range (filas):
                mult[i,:]=np.matmul(llave,matriz[i,:])#mult corresponde a la multiplicacion de cada grupo de 3 por la llave
                matriz2=mult[i,:]%27
                a=0
                while a<columnas:
                    b=matriz2[a] #b muestra datos de la matriz original
                    if b ==0:
                        c='a' #c es variable de mi segunda matriz
                    if b ==1:
                        c='b'
                    if b ==2:
                        c='c'
                    if b ==3:
                        c='d'
                    if b ==4:
                        c='e'
                    if b ==5:
                        c='f'
                    if b ==6:
                        c='g'
                    if b ==7:
                        c='h'
                    if b ==8:
                        c='i'
                    if b ==9:
                        c='j'
                    if b ==10:
                        c='k'
                    if b ==11:
                        c='l'
                    if b ==12:
                        c='m'
                    if b ==13:
                        c='n'
                    if b ==14:
                        c='ñ'
                    if b ==15:
                        c='o'
                    if b ==16:
                        c='p'
                    if b ==17:
                        c='q'
                    if b ==18:
                        c='r'
                    if b ==19:
                        c='s'
                    if b ==20:
                        c='t'
                    if b ==21:
                        c='u'
                    if b ==22:
                        c='v'
                    if b ==23:
                        c='w'
                    if b ==24:
                        c='x'
                    if b ==25:
                        c='y'
                    if b ==26:
                        c='z'
                    if b ==27:
                       c=' '
                    if b ==28:
                       c='.'
                    if b ==29:
                       c=','
                    mensaje.append(c)
                    a=a+1
                    
                i=i+1
            mensajecodificado=''.join(mensaje)
            print('Texto cifrado: '+mensajecodificado)
        if opcion==2:
            salir=1
    except:
        print('\ningrese una opcion valida')