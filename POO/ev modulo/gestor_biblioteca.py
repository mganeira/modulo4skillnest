from pathlib import Path


RUTA_ARCHIVO = Path("biblioteca.txt")
BACKUP_DIR = Path("backups")

class Libro:
    def __init__(self,titulo,autor,anio_publicacion,estado):
        self._titulo = titulo
        self._autor = autor
        self._anio_publicacion = anio_publicacion
        self._estado = estado


    def get_titulo(self):
        return self._titulo

    def set_titulo(self, value):
        self._titulo = value

    def get_autor(self):
        return self._autor

    def set_autor(self, value):
        self._autor = value

    def get_anio(self):
        return self._anio_publicacion
    
    def set_anio(self, value):
        self._anio_publicacion = value

    def get_estado(self):
        return self._estado

    def set_estado(self, value):
        self._estado = value

    def set_titulo(self):
        return self._titulo

    def set_titulo(self, value):
        self._titulo = value

    def __str__():
        ("Título: {titulo}, Autor: {autor}, Año: {anio_publicacion}, Estado: {estado}")

class Biblioteca:
    def __init__(self):
        self._archivo_nombre = "manejo_biblioteca.txt"
        self._libros = []
        self._menu ="""
        "Elige una opción."
        "1:Agregar un libro"
        "2:Eliminar un libro por su título"
        "3:Listar todos los libros disponibles"
        "4:Buscar un libro por su título"
        "5:Marcar un libro como prestado"
        "6:Devolver un libro prestado"
        "7: Salir"
        """

def agregar_libro():
    titulo = input("Título:    ")
    autor = input("Autor:    ")
    anio_publicacion = input("Año de publicación: ")
    estado = input("Estado Disponible / No disponible:           ")
    with RUTA_ARCHIVO.open("a", encoding="utf-8") as f:
        f.write(f"{titulo},{autor},{anio_publicacion},{estado}\n")
    print("Libro registrado.")

def eliminar_libro():
    nombre = input("Nombre del libro a eliminar: ")
    if not RUTA_ARCHIVO.exists():
        print("No hay productos registrados.")
        return
    nuevas = []
    eliminado = False
    with RUTA_ARCHIVO.open("r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(",")
            if len(partes) == 4 and partes[0].lower() == nombre.lower():
                eliminado = True
                continue
            nuevas.append(linea)
    with RUTA_ARCHIVO.open("w", encoding="utf-8") as f:
        f.writelines(nuevas)
    if eliminado:
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")

def listar_libros():
    print("\Listado de libros completo")
    if not RUTA_ARCHIVO.exists():
        print("No hay libros registrados.")
        return
    with RUTA_ARCHIVO.open("r", encoding="utf-8") as f:
        lineas = [l.strip() for l in f if l.strip()]
    if not lineas:
        print("No hay libros registrados.")
        return
    print(f"{'Titulo':<20} {'Autor':<12} {'Año de publicación':<10} {'Estado':<10}")
    for linea in lineas:
        partes = linea.split(",")
        if len(partes) == 4:
            print(f"{partes[0]:<20} {partes[1]:<12} {partes[2]:<10} {partes[3]:<10}")

def buscar_libro():
    nombre = input("Nombre del título del libro a buscar:     ")
    if not RUTA_ARCHIVO.exists():
        print("No hay libros registrados.")
        return
    with RUTA_ARCHIVO.open("r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(",")
            if len(partes) == 4 and partes[0].lower() == nombre.lower():
                print(f"Libro encontrado: Titulo={partes[0]}, Autor={partes[1]}, Año de publicación={partes[2]}, Estado={partes[3]}")
                return
    print("Producto no encontrado.")

#MARCAR LIBRO COMO PRESTADO
def marcar_libro_prestado():
    nombre = input("Nombre del título del libro a prestar: ")
    #Si la ruta no existe, no hay libros registrados, fin.
    if not RUTA_ARCHIVO.exists():
        print("No hay libros registrados.")
        return
    
    # Leer todas las líneas con el método "r", abriendo, leyendo. 
    with RUTA_ARCHIVO.open("r", encoding="utf-8") as f:
        lineas = f.readlines()
    
    # Buscar y modificar el libro. Encontrado se marca como False inicialmente. 


    encontrado = False
    for i, linea in enumerate(lineas):
        partes = linea.strip().split(",")
         # Si se encuentra, for i , lineas in lineas enumeradas,   
         # cada parte (titulo, autor, año de publi, estado) y las separa en partes con split().
        if len(partes) == 4 and partes[0].lower() == nombre.lower(): 
         #Si la parte 0 (el titulo) corresponde al título de nombre que se puso en el input, 
         # y si la parte 4 (indice 3) corresponde a 4, y si esa parte 4 es igual a disponible,
         #  se va a marcar como "no disponible"   

            if partes[3] == "disponible" or partes[3] == "Disponible":
                partes[3] = "no disponible"  
                #Con este join, se transforma de nuevo en cadena lo que se había transformado con split() y lineas[i] van a ser las partes
                lineas[i] = ",".join(partes) + "\n"
                #Se printea lo transformado
                print(f"Libro prestado: Titulo={partes[0]}, Autor={partes[1]}, Año={partes[2]}, Estado={partes[3]}")
                #Encontrado se marca como true
                encontrado = True
                
            else:
                #Si ya está prestado, se printea que está prestado.
                print("El libro ya está prestado.")
                return
            break
    
    if not encontrado:
        print("Libro no encontrado.")
        return
    
    # Guardar los cambios
    with RUTA_ARCHIVO.open("w", encoding="utf-8") as f:
        #Writelines va a sobreescribir las lineas (partes juntadas) nuevas.
        f.writelines(lineas)
            
#MARCAR LIBRO COMO DEVUELTO
def devolver_libro():
    nombre = input("Nombre del título del libro a devolver: ")
    #Si la ruta no existe, no hay libros registrados, fin.
    if not RUTA_ARCHIVO.exists():
        print("No hay libros registrados.")
        return
    
    # Leer todas las líneas con el método "r", abriendo, leyendo. 
    with RUTA_ARCHIVO.open("r", encoding="utf-8") as f:
        lineas = f.readlines()
    
    # Buscar y modificar el libro. Encontrado se marca como False inicialmente. 


    encontrado = False
    for i, linea in enumerate(lineas):
        partes = linea.strip().split(",")
         # Si se encuentra, for i , lineas in lineas enumeradas,   
         # cada parte (titulo, autor, año de publi, estado) y las separa en partes con split().
        if len(partes) == 4 and partes[0].lower() == nombre.lower(): 
         #Si la parte 0 (el titulo) corresponde al título de nombre que se puso en el input, 
         # y si la parte 4 (indice 3) corresponde a 4, y si esa parte 4 es igual a disponible,
         #  se va a marcar como "no disponible"   

            if partes[3] == "no disponible" or partes[3] == "No disponible" or partes[3] == "No Disponible":
                partes[3] = "Disponible"  
                #Con este join, se transforma de nuevo en cadena lo que se había transformado con split()
                lineas[i] = ",".join(partes) + "\n"
                #Se printea lo transformado
                print(f"Libro devuelto: Titulo={partes[0]}, Autor={partes[1]}, Año={partes[2]}, Estado={partes[3]}")
                #Encontrado se marca como true
                encontrado = True
                
            else:
                #Si ya está prestado, se printea que está prestado.
                print("El libro no está prestado.")
                return
            break
    
    if not encontrado:
        print("Libro no encontrado.")
        return
    
    # Guardar los cambios
    with RUTA_ARCHIVO.open("w", encoding="utf-8") as f:
        f.writelines(lineas)
            

def menu():
    while True:
        print("\nMenú:")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Listar libros disponibles")
        print("4. Buscar libros por título")
        print("5. Marcar un libro como prestado")
        print("6. Devolver libro")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            eliminar_libro()
        elif opcion == "3":
            listar_libros()
        elif opcion == "4":
            buscar_libro()
        elif opcion == "5":
            marcar_libro_prestado()
        elif opcion == "6":
            devolver_libro()
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

class LibroDigital(Libro):
    def __init__(self, formato):
        self.formato = formato

    def __str__():
        ("Título: {titulo}, Autor: {autor}, Año: {anio_publicacion}, Estado: {estado}, Formato {formato}")

if __name__ == "__main__":
    menu()