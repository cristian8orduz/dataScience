import random
cartas={"CARTA1" : str(f' _\n|J  |\n| ♦ |\n|J|\n'),
"CARTA2": str(f' _\n|Q  |\n| ♥ |\n|Q|\n'),
"CARTA3" : str(f' _\n|8  |\n| ♣ |\n|8|\n')
}
items = list(cartas.items())
random.shuffle(items)
# Reconstructing the dictionary with shuffled items
cartas_shuffle = dict(items)
print(cartas_shuffle)

key_list=list(cartas_shuffle.keys())
carta_a = random.choice(key_list)
carta_b = random.choice(key_list)
while carta_a == carta_b:                 
    carta_b = random.choice(key_list)
key_list[key_list.index(carta_a)], key_list[key_list.index(carta_b)] = key_list[key_list.index(carta_b)], key_list[key_list.index(carta_a)]
cartas_shuffle = {key: cartas_shuffle[key] for key in key_list}

#aqui se ordenan las llaves
# Extract keys and values
keys = sorted(list(cartas_shuffle.keys()))
values = list(cartas_shuffle.values())
print(keys)
print(values)
# Rebuild the dictionary
#cartas_shuffle = dict(zip(keys, values))

#intercambios.append((carta_a, carta_b))
print(f"Intercambio {carta_a} con {carta_b}")
print(cartas_shuffle)

opciones = ["CARTA1", "CARTA2", "CARTA3"]
reina = str(f' _\n|Q  |\n| ♥ |\n|Q|\n')
respuesta_correcta=None
for key, value in cartas_shuffle.items():
    if value == reina:
        respuesta_correcta = key
        break
print(respuesta_correcta)
respuesta = input(f"¿En cuál de las cartas está la Reina de Corazones? [{', '.join(opciones)}]: ").upper()#duda
print(respuesta)
print(respuesta_correcta)
if respuesta == respuesta_correcta:
    print("¡Felicidades! Has ganado")
else:
    print("Lo siento, has perdido")
