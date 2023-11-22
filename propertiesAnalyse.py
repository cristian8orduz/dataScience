import pandas as pd

# Ruta al archivo CSV
properties_data = pd.read_csv('C:/Users/Usuario/Documents/Codes/python/csvs/properties.csv')

# 1. Conversión de precios a dólares (1 dólar = 83 rupias)
exchange_rate = 83
properties_data['Price (USD)'] = properties_data['Price'] / exchange_rate

# 2. Apartamentos disponibles y media de precios
available_apartments = properties_data[properties_data['Possession Status'].isin(['Ready to Move', 'Immediately'])]
average_price_available = available_apartments['Price (USD)'].mean()

# 3. Inmuebles en el primer piso
first_floor_properties = properties_data[properties_data['Floor No'] == '1']
number_first_floor = first_floor_properties.shape[0]

# 4. Constructor con más edificios
most_common_developer = properties_data['Developer'].value_counts().idxmax()
most_common_developer_count = properties_data['Developer'].value_counts().max()

# 5. Cantidad de casas disponibles
total_units_available = properties_data['Units Available'].sum()

# 6. Locales comerciales
commercial_properties = properties_data[properties_data['Commercial'] == 'Y']

# 7. Inmueble más costoso y más barato
most_expensive_property = properties_data.loc[properties_data['Price (USD)'].idxmax()]
cheapest_property = properties_data.loc[properties_data['Price (USD)'].idxmin()]

# 8. Inmuebles en construcción por Kalpataru Ltd.
kalpataru_construction_properties = properties_data[
    (properties_data['Developer'] == 'Kalpataru Ltd.') & 
    (properties_data['Possession Status'] == 'Under Construction')
]

# Resultados
print("Media de precios de apartamentos disponibles:", average_price_available)
print("Número de inmuebles en el primer piso:", number_first_floor)
print("Constructor con más edificios:", most_common_developer, "con", most_common_developer_count, "edificios")
print("Total de casas disponibles:", total_units_available)
print("Inmueble más costoso y más barato:", most_expensive_property['ID'], cheapest_property['ID'])
print("Primeros 5 locales comerciales:", commercial_properties.head())
print("Primeros 5 inmuebles en construcción por Kalpataru Ltd.:", kalpataru_construction_properties.head())
