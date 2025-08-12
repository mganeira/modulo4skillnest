import csv

mas_bicicletas = [
    ["Trek", "Marlin 8", 29, 850000],
    ["Giant", "Talon 4", 27.5, 720000],
    ["Scott", "Aspect 1050", 29, 900000],
    ["Oxford", "Top Mega 1", 26, 350000],
    ["Bianchi", "Impulso 2", 28, 1200000]
]
with open('bicicletas_nuevo.csv', 'a', newline='', encoding='utf-8') as archivo:
    escritor = csv.writer(archivo) # Crea un objeto escritor para escribir en el archivo
    escritor.writerows(mas_bicicletas) # Escribe múltiples filas de datos