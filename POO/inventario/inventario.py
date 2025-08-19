import csv
from pathlib import Path

nombre_a = 'inventario_bicicletas.csv'
ruta_din = 'inventario/' + nombre_a
campos = ["marca", "modelo", "aro", "precio"]

def inicializar_a(ruta_din: Path):
    with open(ruta_din, 'w', newline= '', encoding= 'utf-8') as archivo:
        writer = csv.DictWriter(archivo, fieldnames= campos)
        writer.writeheader()
        print(f"Archivo '{nombre_a}' inicializado correctamente.")

inicializar_a(ruta_din)