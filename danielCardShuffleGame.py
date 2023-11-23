import random

# Inicializar variables
cartas = ["carta izquierda (I)","carta del medio (M)", "carta derecha (D)"]
cartas_letras = ["8", "Q", "J"]
cartas_simbolos = ["♣", "♥", "♦"]

def main():
    # con global, se usan las variables declaradas arriba
    global cartas, cartas_letras, cartas_simbolos
    nombre = None
    print("Adivina dónde está la Reina de Corazones")
    while True:        
        opcion = input("Seleccione jugar [J], tabla de posiciones [T], salir [S]:")

        if opcion == "J":
            if nombre is None: 
              nombre = input("Por favor, indique su nombre: ")            
            
            # unir listas temporalmente para hacer el shuffle en el mismo orden para letra y símbolo
            lista_completa = list(zip(cartas, cartas_letras, cartas_simbolos))
            random.shuffle(lista_completa)
            cartas, cartas_letras, cartas_simbolos = zip(*lista_completa)
            # Convertir a listas nuevamente
            cartas = list(cartas)
            cartas_letras = list(cartas_letras)
            cartas_simbolos = list(cartas_simbolos)
            
            #print(cartas)
            #print(cartas_letras)
            #print(cartas_simbolos)
            
            print(f"{nombre}, mantén tus ojos bien abiertos mientras las cartas se mueven")
            # Mostrar las cartas en su orden
            dibujar_cartas()
            input("Presiona ENTER cuando estés listo(a)")
            
            num_intercambios = random.randint(2, 4)
            intercambios = []  
            for _ in range(num_intercambios):
                carta_a = random.choice(cartas)
                carta_b = random.choice(cartas)
                while carta_a == carta_b:                 
                    carta_b = random.choice(cartas)
                index_a = cartas.index(carta_a)
                index_b = cartas.index(carta_b)
                
                # intercambiar cartas
                cartas[index_a], cartas[index_b] = cartas[index_b], cartas[index_a]
                # intercambiar letras y símbolos
                cartas_letras[index_a], cartas_letras[index_b] = cartas_letras[index_b], cartas_letras[index_a]
                cartas_simbolos[index_a], cartas_simbolos[index_b] = cartas_simbolos[index_b], cartas_simbolos[index_a]
                #intercambios.append((carta_a, carta_b))
                print(f"Intercambio {carta_a} con {carta_b}")
                #print(cartas)

            # No es necesario, ya que se muestra en el ciclo de arriba
            #random.shuffle(intercambios)
            #for intercambio in intercambios:
            #    carta_a, carta_b = intercambio
            #    print(f"Intercambio {carta_a} con {carta_b}")

            opciones = ["I", "M", "D"]
            respuesta_correcta = int(cartas.index("carta del medio (M)"))
            respuesta = input(f"¿En cuál de las cartas está la Reina de Corazones? [{', '.join(opciones)}]: ")
            respuesta_index = opciones.index(respuesta)

            if respuesta_index == respuesta_correcta:
                print("¡Felicidades! Has ganado")
            else:
                print("Lo siento, has perdido")

            # mostrar cartas para verificar el resultado
            dibujar_cartas()
            
        elif opcion == "T":
            print("En la tercera sustentación se va a ver reflejado.")

        elif opcion == "S":
            print("Adiós.")
            break

        else:
            print("Error.")

def dibujar_cartas():
    global cartas_letras, cartas_simbolos
    print(" ___   ___   ___")
    print("|" + cartas_letras[0] + "  | |" + cartas_letras[1] + "  | |" + cartas_letras[2] + "  |")
    print("| " + cartas_simbolos[0] + " | | " + cartas_simbolos[1] + " | | " + cartas_simbolos[2] + " |")
    print("|__" + cartas_letras[0] + "| |__" + cartas_letras[1] + "| |__" + cartas_letras[2] + "|")

#if _name_ == "_main_":
#    main()
main()
