import numpy as np
from os import system
#from VALID import binn, ns
salir=0
system("cls")

while salir==0:
        print('\n----Codigo hamming----')
        print('(1) Iniciar programa ')
        print('(2) salir ')
        opcion=int(input('ingrese una opcion: '))
        pasouno=[]
        binario=[]
        if opcion==1:
                i=0
                texto=input("\n Ingrese el texto a transmitir: ")
                
                #np.zeros([len(texto),7])#filas,columnas
                m=0
                
                while i<len(texto):#guarda en el vector b la representacionen binario de cada caracter
                        j=texto[i]
                        b=bin(ord(j))
                        print(b)
                        i=i+1
                        
                        k=0
                        while k<len(b):#guarda en el vector binario la separacion del numero binario b
                                l=b[k]
                                binario.append(l)
                                k=k+1
                        binario.remove('b')    
                        pasouno.append(b.replace('b',''))
                        
                 
                print("la traduccion a binario del texto es: ")
                print(binario)
                #print(pasouno)
                acumulado=0
                p1=0
                i=1
                posicion=0
                j=0
                x=0
                while (pow(2,j))<=len(binario):#inserta bits de paridad en 1,2,4,8,16...
                        x=(pow(2,j)-1)
                        binario.insert(x,"p")
                        j=j+1
                        print(x)
                        print(binario[-1])



                #while ((2*i)+1)<=len(binario):
                        #posicion=((2*i)+1)
                        #p1=p1+int(binario[posicion-1])
                        #i=i+1  
                        #print('posicion')
                        #print(posicion)
                        #print('valor de laposicion')
                        #print(binario[posicion-1])   
                
                #print(p1)#3,5,7,9,11...(2n+1)
                if p1%2==0: 
                        binario.insert (0,1)#si es par inserta uno en posicion 0
                if p1%2!=0: 
                        binario.insert (0,0)#si es impar inserta 0 en posicion 0
                print(binario)




        if opcion==2:
                salir=1
