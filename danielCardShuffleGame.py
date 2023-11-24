import random

# Inicializar variables
carta1 = " ___\n|J  |\n| ♦ |\n|__J|\n"
carta2 = " ___\n|Q  |\n| ♥ |\n|__Q|\n"
carta3 = " ___\n|8  |\n| ♣ |\n|__8|\n"
cartas_lista=list(carta1,carta2,carta3)
cartas_den=("Jota","Reina","Ocho")
def main():
    # con global, se usan las variables declaradas arriba
    global cartasList
    nombre = None
    print("Adivina dónde está la Reina de Corazones")
    while True:        
        opcion = input("Seleccione jugar [J], tabla de posiciones [T], salir [S]:").upper()

        if opcion == "J":
            if nombre is None: 
              nombre = input("Por favor, indique su nombre: ")            
            
            # unir listas temporalmente para hacer el shuffle en el mismo orden para letra y símbolo
            lista_completa = list(zip(carta_lista, cartas_den))
            random.shuffle(lista_completa)
            cartas_lista_final, cartas_den_final = zip(*lista_completa)
            # Convertir a listas nuevamente
            cartas_lista_final = list(cartas_lista_final)
            cartas_den_final = list(cartas_den_final)
            
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
                carta_a1 = random.choice(cartas_den_final)
                carta_b1 = random.choice(cartas_den_final)
                while carta_a == carta_b:                 
                    carta_b = random.choice(cartas_den_final)
                index_a = cartas_den_final.index(carta_a)
                index_b = cartas_den_final.index(carta_b)
                carta_a2 = cartas_lista_final[index_a]
                carta_b2 = cartas_lista_final[index_b]
                print(carta_a1, carta_a2)
                print(carta_b1, carta_b2)
                
                # intercambiar cartas
                cartas_den_final[index_a], cartas_den_final[index_b] = carta_b1, carta_a1
                # intercambiar letras y símbolos
                cartas_lista_final[index_a], cartas_lista_final[index_b] = carta_b2, carta_a2
                #intercambios.append((carta_a, carta_b))
                print(f"Intercambio {carta_a} con {carta_b}")
                dibujar_cartas()
                #print(cartas)

            # No es necesario, ya que se muestra en el ciclo de arriba
            #random.shuffle(intercambios)
            #for intercambio in intercambios:
            #    carta_a, carta_b = intercambio
            #    print(f"Intercambio {carta_a} con {carta_b}")

            opciones = ["I", "M", "D"]
            respuesta_correcta = int(cartas.index("carta del medio (M)"))
            respuesta = input(f"¿En cuál de las cartas está la Reina de Corazones? [{', '.join(opciones)}]: ")
            respuesta_index = opciones.index(respuesta)#colocarlo como un entero

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
