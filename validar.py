# FUNCIÓN validar con valores

def validar(valida, valor):  # validación de variable entero
    if valor == 1:
        while True:
            if valida.isdigit():
                valida = int(valida)
                return (valida)
                break #salida del while
            else:
                print('Debes escribir un número entero!')
                print('-------------------------------')
                valida = input('¡Error! Digite número: ')

    # validación de la variable vacía
    elif valor == 2:
        while True:
            if len(valida) > 0:
                valida = str(valida)
                return valida
                break
            else:
                print('Debes escribir texto en esta opción!')
                print('------------------------------------')
                valida = input('¡Error! Digite Texto: ')

    # Función que valida un número flotante
def valFloat(valida):
    while True:
        try:
            valida = float(valida)
            return valida
        except ValueError:
            print('Debes digitar un número flotante.')
            print('----------------------------------')
            valida = input('Error!, Digite el tipo de dato solicitado: ')


            
