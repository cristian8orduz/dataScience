import random
cartas={"Jota" : str(f' ___\n|J  |\n| ♦ |\n|__J|\n'),
"Reina": str(f' ___\n|Q  |\n| ♥ |\n|__Q|\n'),
"Ocho" : str(f' ___\n|8  |\n| ♣ |\n|__8|\n')
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
key_list[carta_a], key_list[carta_b] = key_list[carta_b], key_list[carta_a]
cartas_shuffle = {key: cartas_shuffle[key] for key in key_list}
#intercambios.append((carta_a, carta_b))
print(f"Intercambio {carta_a} con {carta_b}")
print(cartas_shuffle)
