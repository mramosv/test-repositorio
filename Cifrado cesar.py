palabra = input("Ingrese frase a codificar por favor: ")
total = [chr(ord(letra)+3) for letra in palabra]
concatenacion = ''.join(total)  
print("El cifrado cesar es:",concatenacion)