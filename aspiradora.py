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
        # Localizacion A esta sucio.
        print("La aspiradora esta puesto en el cuarto A")
        if estado == '1':
            print("Cuarto A esta sucio")
            # Limpiar suciedad y reportarlo limpio
            cuarto_estado['A'] = '0'
            #  cost += 1  # cost for suck
            #  print("Cost for CLEANING A " + str(cost))
            print("El cuarto A ha sido limpiado")

            if segundo_estado == '1':
                # Si B esta sucio.
                print("El cuarto B esta sucio")
                print("Moviendose a la derecha al cuarto B")
                #  cost += 1  # cost for moving right
                #  print("COST for moving RIGHT" + str(cost))
                # Limpiar suciedad y reportarlo limpio
                cuarto_estado['B'] = '0'
                #  cost += 1  # cost for suck
                #  print("COST for SUCK " + str(cost))
                print("Cuarto B ha sido limpiado")
            else:
                #  print("No action" + str(cost))
                # Limpiar suciedad y reportarlo como limpio.
                print("El cuarto B ya esta limpio")

        if estado == '0':
            print("El cuarto A ya esta limpio")
            if segundo_estado == '1':  # Si B esta sucio
                print("El cuarto B est sucio")
                print("Moviendo a la DERECHA al cuarto B")
                #  cost += 1  # cost for moving right
                #  print("COST for moving RIGHT " + str(cost))
                # suck the dirt and mark it as clean
                cuarto_estado['B'] = '0'
                #  cost += 1  # cost for suck
                #  print("Cost for SUCK" + str(cost))
                print("Cuarto B ya ha sido limpiado")
            else:
                #  print("No action " + str(cost))
                #  print(cost)
                # Limpiar y marcar como limpio.
                print("El cuarto B ya esta limpio")

    else:
        print("La aspiradora esta en el cuarto B")
        # CUarto B esta sucio
        if estado == '1':
            print("Cuarto B esta sucio")
            # Limpiar suciedad y marcar como limpio.
            cuarto_estado['B'] = '0'
            #  cost += 1  # cost for suck
            #  print("COST for CLEANING " + str(cost))
            print("Cuarto B ha sido limpiado")

            if segundo_estado == '1':
                # Si A esta sucio
                print("Cuarto A esta sucio")
                print("Moviendo a la izquierda la cuarto A")
                #  cost += 1  # cost for moving right
                #  print("COST for moving LEFT" + str(cost))
                # Limpiar suciedad y marcar como limpio.
                cuarto_estado['A'] = '0'
                #  cost += 1  # cost for suck
                #  print("COST for SUCK " + str(cost))
                print("Cuarto A ha sido limpiado")

        else:
            #  print(cost)
            # Limpiar y marcar como limpio
            print("Cuarto B ya esta limpio")

            if segundo_estado == '1':  # Si A esta sucio
                print("Cuarto A esta sucio")
                print("Moviendose a la izquierda al cuarto A")
                #  cost += 1  # cost for moving right
                #  print("COST for moving LEFT " + str(cost))
                # suck the dirt and mark it as clean
                cuarto_estado['A'] = '0'
                #  cost += 1  # cost for suck
                #  print("Cost for SUCK " + str(cost))
                print("Cuarto A ha sido limpiado")
            else:
                #  print("No action " + str(cost))
                # suck and mark clean
                print("Cuarto A ya esta limpio")

    # done cleaning
    print("ESTADO FINAL DEL CUARTO")
    print(cuarto_estado)
    #  print("Performance Measurement: " + str(cost))

aspiradora()