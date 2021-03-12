# INSTRUCCIONES
#Ingresar localización: A o B, en letras mayúsculas
#Ingresar el estado: 1 o 0, donde 1 es sucio y 0 es limpio.

def aspiradora():
    cuarto_estado = {'A': '0', 'B': '0'}
    #  cost = 0

    localizacion_inicial = input("Ingrese la localizacion de la aspiradora: ")  # user_input of location vacuum is placed
    estado = input("Ingrese el estado de: " + localizacion_inicial)  # user_input if location is dirty or clean
    segundo_estado = input("Ingrese el estado del otro cuarto: ")
    print("Estado inicial del cuarto: " + str(cuarto_estado))

    if localizacion_inicial == 'A':
        print("La aspiradora esta puesto en el cuarto A")
        if estado == '1':
            print("Cuarto A esta sucio")
            cuarto_estado['A'] = '0'
            print("El cuarto A ha sido limpiado")

            if segundo_estado == '1':
                print("El cuarto B esta sucio")
                print("Moviendose a la derecha al cuarto B")
                cuarto_estado['B'] = '0'
                print("Cuarto B ha sido limpiado")
            else:
                print("El cuarto B ya esta limpio")

        if estado == '0':
            print("El cuarto A ya esta limpio")
            if segundo_estado == '1':
                print("El cuarto B est sucio")
                print("Moviendo a la DERECHA al cuarto B")
                cuarto_estado['B'] = '0'
                print("Cuarto B ya ha sido limpiado")
            else:
                print("El cuarto B ya esta limpio")

    else:
        print("La aspiradora esta en el cuarto B")
        if estado == '1':
            print("Cuarto B esta sucio")
            cuarto_estado['B'] = '0'
            print("Cuarto B ha sido limpiado")

            if segundo_estado == '1':
                print("Cuarto A esta sucio")
                print("Moviendo a la izquierda la cuarto A")
                cuarto_estado['A'] = '0'
                print("Cuarto A ha sido limpiado")

        else:
            print("Cuarto B ya esta limpio")

            if segundo_estado == '1':
                print("Cuarto A esta sucio")
                print("Moviendose a la izquierda al cuarto A")
                cuarto_estado['A'] = '0'
                print("Cuarto A ha sido limpiado")
            else:
                print("Cuarto A ya esta limpio")

    print("ESTADO FINAL DEL CUARTO")
    print(cuarto_estado)

aspiradora()