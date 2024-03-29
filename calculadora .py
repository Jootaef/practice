print('Calculadora con una sola variable')

print('\n~~~~~~~~~~~~~~~~~~')
print('Menú de opcipnes')
print('~~~~~~~~~~~~~~~~~~')
print('1. Suma\n2. Resta \n3. Multiplicación \n4. División \n5. División entera \n6. Exponente \n7. Modulo o resto')
opcion_deseada = int(input('Introduce la opción deseada:'))
if opcion_deseada == 1:
    print('Escogiste Suma')
    first_number_suma = int(input('Introduce el primer número:'))
    second_number_suma = int(input('Introduce el segundo número:'))
    resultado_suma = first_number_suma + second_number_suma
    print(f'El resultado de la suma es {resultado_suma}')
elif opcion_deseada == 2:
    print('Escogiste resta')
    first_number_resta = int(input('Introduce el primer número:'))
    second_number_resta = int(input('Introduce el segundo número:'))
    resultado_resta = first_number_resta - second_number_resta
    print(f'El resultado de la resta es {resultado_resta}')
elif opcion_deseada == 3:
    print('Escogiste Multiplicación')
    first_number_multiplicacion = int(input('Introduce el primer número:'))
    second_number_multiplicacion = int(input('Introduce el segundo número:'))
    resultado_multiplicacion = first_number_multiplicacion * second_number_multiplicacion
    print(f'El resultado de la multiplicacion es {resultado_multiplicacion}')
elif opcion_deseada == 4:
    print('Escogiste División')
    first_number_division = int(input('Introduce el primer número:'))
    second_number_division = int(input('Introduce el segundo número:'))
    resultado_division = first_number_division / second_number_division
    print(f'El resultado  es {resultado_division}')
elif opcion_deseada == 5:
    print('Escogiste División entera')
    first_number_división_entera = int(input('Introduce el primer número:'))
    second_number_división_entera = int(input('Introduce el segundo número:'))
    resultado_división_entera = first_number_división_entera // second_number_división_entera
    print(f'El resultado es {resultado_división_entera}')
elif opcion_deseada == 6:
    print('escogiste Exponente')
    first_number_exponente = int(input('Introduce el primer número:'))
    second_number_exponente = int(input('Introduce el segundo número:'))
    resultado_exponente = first_number_exponente ** second_number_exponente
    print(f'El resultado es {resultado_exponente}')
elif opcion_deseada == 7:
    print('Escogiste Modulo o resto')
    first_number_modulo = int(input('Introduce el primer número:'))
    second_number_modulo = int(input('Introduce el segundo número:'))
    resultado_modulo = first_number_modulo % second_number_modulo
    print(f'El resultado es {resultado_modulo}')
else:
    print('Opcion invalida')