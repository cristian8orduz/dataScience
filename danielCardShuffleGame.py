import random
import datetime
import json
cartas={"CARTA1": str(f' _\n|J  |\n| ♦ |\n|  J|  '),
        "CARTA2": str(f' _\n|Q  |\n| ♥ |\n|  Q|  '),
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
            record = [nombre, puntos, fecha]
            file_path = ''#aqui va la direccion del JSON para ingresar
            try:
                with open(file_path, 'r') as file:
                    tabla = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                tabla = []
            record_exists = False
            for existente in tabla:
                if existente[0] == nombre:  # Name is at index 0
                    record_exists = True
                    if record[1] > existente[1]:  # Points are at index 1
                        existente[1] = record[1]
                        existente[2] = record[2]  # Update date and time
                    break
            if not record_exists:
                tabla.append(record)
            
            # Sort the list in descending order by points
            tabla.sort(key=lambda x: x[1], reverse=True)
            
            # Write the updated data back to the file
            with open(file_path, 'w') as file:
                json.dump(tabla, file)
        elif opcion == "T":
                print("En la tercera sustentación se va a ver reflejado.")
                with open(file_path, 'w') as file:
                        for
                

        elif opcion == "S":
            print("Adiós.")
            break

        else:
            print("Error.")


#if _name_ == "_main_":
#    main()
main()
