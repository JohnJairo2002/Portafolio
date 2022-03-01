# El ciclo for ejecuta un bloque de código repetidamente hasta que
# la condición en el ciclo for no sea válida

mascotas = ['gatos', 'perros', 'perros', 'loros', 'peces']

for i in mascotas:
    print(i)

contador_gatos = 0
contador_perros = 0
contador_peces = 0


for i in mascotas:
    if i == "gatos":
        contador_gatos = contador_gatos + 1

    if i == "perros":
        contador_perros = contador_perros + 1

    if i == "peces":
        contador_peces = contador_peces +1 

print("El numero de gatos es:", contador_gatos)
print("El numero de perros es:", contador_perros)
print("El numero de peces es:", contador_peces)