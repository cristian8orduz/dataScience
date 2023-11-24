import random
import datetime
import json
cartas={"CARTA1": str(f' _\n|J  |\n| ♦ |\n|  J|\n'),
        "CARTA2": str(f' _\n|Q  |\n| ♥ |\n|  Q|\n'),
        "CARTA3": str(f' _\n|8  |\n| ♣ |\n|  8|\n')}
def main():
    # con global, se usan las variables declaradas arriba
    global cartas
    nombre = None
        puntos=0
    print("Adivina dónde está la Reina de Corazones")
    while True:        
        opcion = input("Seleccione jugar [J], tabla de posiciones [T], salir [S]:").upper()

        if opcion == "J":
            if nombre is None: 
              nombre = input("Por favor, indique su nombre: ")            
            
            items = list(cartas.items())
            random.shuffle(items)
            # Reconstructing the dictionary with shuffled items
            cartas_shuffle = dict(items)
            
            print(f"{nombre}, mantén tus ojos bien abiertos mientras las cartas se mueven")
            # Mostrar las cartas en su orden
            print(cartas_shuffle["CARTA1"],cartas_shuffle["CARTA2"],cartas_shuffle["CARTA3'])
            input("Presiona ENTER cuando estés listo(a)")
            
            num_intercambios = random.randint(5, 8)
            intercambios = []  
            for _ in range(num_intercambios):
                    key_list=list(cartas_shuffle.keys())
                    carta_a = random.choice(key_list)
                    carta_b = random.choice(key_list)
                    while carta_a == carta_b:                 
                        carta_b = random.choice(key_list)
                    key_list[key_list.index(carta_a)], key_list[key_list.index(carta_b)] = key_list[key_list.index(carta_b)], key_list[key_list.index(carta_a)]
                    cartas_shuffle = {key: cartas_shuffle[key] for key in key_list}
                    #se reordenan las llaves de las cartas
                    keys = sorted(list(cartas_shuffle.keys()))
                    values = list(cartas_shuffle.values())
                    print(keys)
                    print(values)
                    # Rebuild the dictionary
                    cartas_shuffle = dict(zip(keys, values))
                        #intercambios.append((carta_a, carta_b))
                    print(f"Intercambio {carta_a} con {carta_b}")


            opciones = ["CARTA1", "CARTA2", "CARTA3"]
            reina = str(f' _\n|Q  |\n| ♥ |\n|Q|\n')
            respuesta_correcta=None
            for key, value in cartas_shuffle.items():
                if value == reina:
                    respuesta_correcta = key
                    break
            respuesta = input(f"¿En cuál de las cartas está la Reina de Corazones? [{', '.join(opciones)}]: ").upper()#duda
            if respuesta == respuesta_correcta:
                print("¡Felicidades! Has ganado")
                puntos+=1
            else:
                print("Lo siento, has perdido")
            ya=datetime.now()
            fecha=ya.strftime('%d-%m-%Y a las %I:%M %p')
            def read_and_update_or_append(file_path, new_name, new_number):
            found = False
            updated_lines = []
        
            try:
                with open(file_path, 'r') as file:
                    for line in file:
                        nombreAnt, puntosAnt,fechaAnt = line.strip().split('!')
                        if nombre == nombreAnt:
                            found = True
                            # Update the number if the name matches
                            updated_lines.append(f"{nombre}!{new_number}!{fecha}\n")
                        else:
                            updated_lines.append(line)
        
                # If found, rewrite the file with updated data
                if found:
                    with open(file_path, 'w') as file:
                        file.writelines(updated_lines)
                else:
                    # If not found, append the new record
                    with open(file_path, 'a') as file:
                        file.write(f"{nombre}!{puntos}!{fecha}\n")
        
                return found
        
            except FileNotFoundError:
                # Create the file and write the new record if file does not exist
                with open(file_path, 'w') as file:
                    file.write(f"{new_name}!{new_number}\n")
                return False

        elif opcion == "T":
                print("En la tercera sustentación se va a ver reflejado.")
                with open(file_path, 'w') as file:
                        tabla=json.load(file)
                for existente in tabla:
                        i=1
                        print(str(i)+", "+existente[0]+", "+existente[1]", puntos. Mejor ugada el "+existente[3])
                        i+=1
                

        elif opcion == "S":
            print("Adiós.")
            break

        else:
            print("Error.")


#if _name_ == "_main_":
#    main()
main()
