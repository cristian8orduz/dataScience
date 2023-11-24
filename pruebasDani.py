import random
cartas={"Carta1" : str(f' _\n|J  |\n| ♦ |\n|J|\n'),
"Carta2": str(f' _\n|Q  |\n| ♥ |\n|Q|\n'),
"Carta3" : str(f' _\n|8  |\n| ♣ |\n|8|\n')
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
keys = list(cartas_shuffle.keys()).sort()
values = list(cartas_shuffle.values())
print(keys)
print(values)
# Rebuild the dictionary
#cartas_shuffle = dict(zip(keys, values))

#intercambios.append((carta_a, carta_b))
print(f"Intercambio {carta_a} con {carta_b}")
print(cartas_shuffle)
