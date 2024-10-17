import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Ingresa tu longitud de contraseña: "))
resultado = ""

for i in range(longitud):
    resultado += random.choice(caracteres)
    
print(f"Tu contraseña con longitud {longitud} es: {resultado}")
