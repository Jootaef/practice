print('Menu de opciones')
print('ingrese el # 2 si prefiere comer helado ')
print('ingrese el # 1 si prefiere comer pastel ')
opcion =  int(input('Cuál es tu opción?'))


if opcion == 1:
    print('\nEntonces iremos a comer pastel')
    print('\nTenemos 3 tipos de sabores: vainilla, chocolate y manjar')
    pastel = input('\nQué clase de pastel te gustaria?')
    if pastel == 'vainilla':
        print('\nlisto entonces iremos a comer helado de vainilla')
    elif pastel == 'chocolate':
        print('\nlisto entonces iremos a comer helado de chocolate')
    elif pastel == 'manjar':
        print('\nlisto entonces iremos a comer helado de manjar')
    else:
        print('\nlo siento eso no es una opción valida')


elif opcion == 2:
    print('\nEntonces iremos a comer helado')
else:
    print('opcion invalida')

