contador = int(input('coloca un numero menor a 10:')) 
while contador < 10: 
    contador += 1
    print('El contador actual es', contador)
    if contador == 9: 
        break
print('Se ha ejecutado la sentencia break')