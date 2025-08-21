from pathlib import Path

from pathlib import Path

# Carpeta del script actual
BASE_DIR = Path(__file__).resolve().parent

# Archivo de la biblioteca
RUTA_ARCHIVO = BASE_DIR / "biblio.txt"
print("Ruta absoluta esperada:", RUTA_ARCHIVO.resolve())
print("¿Existe el archivo?:", RUTA_ARCHIVO.exists())

class Libro:
    def __init__(self, titulo, autor, anio_publicacion, estado):
        self._titulo = titulo
        self._autor = autor
        self._anio_publicacion = anio_publicacion
        self._estado = estado
#Getters y setters
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
#Definición de formato por defecto
    def __str__(self):
        return f"Título: {self._titulo}, Autor: {self._autor}, Año: {self._anio_publicacion}, Estado: {self._estado}"
    
#Creación de clase Biblioteca
class Biblioteca:
    def __init__(self):
        self._archivo_nombre = "biblio.txt"
        self._libros = []  # Lista de objetos Libro vacía
        self._menu = """
        "Elige una opción."
        "1:Agregar un libro"
        "2:Eliminar un libro por su título"
        "3:Listar todos los libros disponibles"
        "4:Buscar un libro por su título"
        "5:Marcar un libro como prestado"
        "6:Devolver un libro prestado"
        "7: Salir"
        """
    #Lo primero, cargar libros desde el txt 
    def cargar_libros_desde_archivo(self):
        """Carga los libros desde el archivo al iniciar el programa"""
        #Si no está el archivo biblio.txt en la ruta, no existe
        if not RUTA_ARCHIVO.exists():
            print("No se encontró archivo de biblio. Iniciando con biblioteca vacía.")
            return

        try:
            #Se abre la ruta del archivo con método "r" de lectura
            with RUTA_ARCHIVO.open("r", encoding="utf-8") as f:
                #Recorre las lineas en el archivo que está leyendo
                for linea in f:
                    #Por cada linea, elimina los espacios vacíos
                    linea = linea.strip()
                    if linea:
                        #Si hay texto, separa la linea en 4 partes ( 4 encabezados)
                        partes = linea.split(",")
                        if len(partes) == 4:
                            #Se crea un objeto libro con las partes separadas por coma
                            libro = Libro(partes[0], partes[1], partes[2], partes[3].lower())
                            #Se añade a la lista de libros de la biblioteca
                            self._libros.append(libro)
            print(f"Se cargaron {len(self._libros)} libros desde el archivo.")
        except Exception as e:
            print(f"Error al cargar libros: {e}")

    def guardar_libros_en_archivo(self):
        """Guarda todos los libros en el archivo al finalizar el programa"""
        try:
            #Con el método open y write, se escribe la lista en el archivo con los getters.
            with RUTA_ARCHIVO.open("w", encoding="utf-8") as f:
                for libro in self._libros:
                    f.write(f"{libro.get_titulo()},{libro.get_autor()},{libro.get_anio()},{libro.get_estado()}\n")
            print(f"Se guardaron {len(self._libros)} libros en el archivo.")
        except Exception as e:
            print(f"Error al guardar libros: {e}")

    def agregar_libro(self):
        """Agrega un nuevo libro a la biblioteca"""
        titulo = input("Título:    ")
        autor = input("Autor:    ")
        anio_publicacion = input("Año de publicación: ")
        estado = input("Estado Disponible / No disponible:   ").strip().lower()
        
        #Se crea objeto libro y se añade a la lista
        libro = Libro(titulo, autor, anio_publicacion, estado)
        self._libros.append(libro)
        
        #Guardar inmediatamente en el archivo
        self.guardar_libros_en_archivo()
        print("Libro registrado y guardado.")

    def eliminar_libro(self):
        """Elimina un libro de la biblioteca por título"""
        nombre = input("Nombre del libro a eliminar: ")
        if not self._libros:
            print("No hay libros registrados.")
            return
        
        #Se busca el libro en la lista y se elimina
        eliminado = False
        for i, libro in enumerate(self._libros):
            if libro.get_titulo().lower() == nombre.lower():
                self._libros.pop(i)
                eliminado = True
                break
        
        if eliminado:
            #Guardar cambios inmediatamente en el archivo
            self.guardar_libros_en_archivo()
            print("Libro eliminado y cambios guardados.")
        else:
            print("Libro no encontrado.")

    def listar_libros(self):
        """Lista todos los libros de la biblioteca"""
        print("\nListado de libros completo")
        if not self._libros:
            print("No hay libros registrados.")
            return
        
        #Se muestran todos los libros de la lista con formato de tabla
        print(f"{'Título':<20} {'Autor':<15} {'Año de publicación':<18} {'Estado':<15}")
        print("-" * 70)
        for libro in self._libros:
            print(f"{libro.get_titulo():<20} {libro.get_autor():<15} {libro.get_anio():<18} {libro.get_estado():<15}")
#Método buscar para buscar y gestionar 
    def buscar_libro_por_titulo(self, titulo):
        """Busca un libro en la biblioteca por título y devuelve el objeto Libro"""
        #Recorre la lista de libros buscando por título
        for libro in self._libros:
            if libro.get_titulo().lower() == titulo.lower():
                return libro
        return None
#Método buscar de la interfaz
    def buscar_libro(self):
        """Interfaz para buscar un libro por título"""
        nombre = input("Nombre del título del libro a buscar:     ")
        if not self._libros:
            print("No hay libros registrados.")
            return
        
        #Usa el método de búsqueda interno
        libro = self.buscar_libro_por_titulo(nombre)
        if libro:
            print(f"Libro encontrado: Titulo={libro.get_titulo()}, Autor={libro.get_autor()}, Año de publicación={libro.get_anio()}, Estado={libro.get_estado()}")
        else:
            print("Libro no encontrado.")

    def marcar_libro_prestado(self):
        """Marca un libro como prestado - Colaboración entre objetos"""
        nombre = input("Nombre del título del libro a prestar: ")
        #Si no hay libros en la lista, no hay libros registrados, fin.
        if not self._libros:
            print("No hay libros registrados.")
            return
        
        #Buscar el libro usando el método interno de búsqueda
        libro = self.buscar_libro_por_titulo(nombre)
        
        if libro:
            #Colaboración: La biblioteca opera sobre el objeto libro
            if libro.get_estado().lower() in ["disponible"]:
                libro.set_estado("no disponible")  # Modifica el estado del objeto
                #Guardar cambios inmediatamente en el archivo
                self.guardar_libros_en_archivo()
                print(f"Libro prestado: Titulo={libro.get_titulo()}, Autor={libro.get_autor()}, Año={libro.get_anio()}, Estado={libro.get_estado()}")
            else:
                #Si ya está prestado, se printea que está prestado.
                print("El libro ya está prestado.")
        else:
            print("Libro no encontrado.")

    def devolver_libro(self):
        """Devuelve un libro prestado - Colaboración entre objetos"""
        nombre = input("Nombre del título del libro a devolver: ")
        #Si no hay libros en la lista, no hay libros registrados, fin.
        if not self._libros:
            print("No hay libros registrados.")
            return
        
        #Buscar el libro usando el método interno de búsqueda
        libro = self.buscar_libro_por_titulo(nombre)
        
        if libro:
            #Colaboración: La biblioteca opera sobre el objeto libro
            if libro.get_estado().lower() in ["no disponible"]:
                # Modifica el estado del objeto
                libro.set_estado("disponible")

                #Guardar cambios inmediatamente en el archivo
                self.guardar_libros_en_archivo()
                print(f"Libro devuelto: Titulo={libro.get_titulo()}, Autor={libro.get_autor()}, Año={libro.get_anio()}, Estado={libro.get_estado()}")
            else:
                #Si no está prestado, se printea que no está prestado.
                print("El libro no está prestado.")
        else:
            print("Libro no encontrado.")

#Métodos de gestión para obtener estadísticas
    def obtener_libros_por_estado(self, estado):
        """Método de colaboración: Recorre la lista y filtra libros por estado"""
        libros_filtrados = []
        #Recorre todos los libros y filtra por estado
        for libro in self._libros:
            if libro.get_estado().lower() == estado.lower():
                libros_filtrados.append(libro)
        return libros_filtrados

    def contar_libros_disponibles(self):
        """Método de colaboración: Cuenta cuántos libros están disponibles"""
        contador = 0
        #Recorre la lista de libros y cuenta los disponibles
        for libro in self._libros:
            if libro.get_estado().lower() == "disponible":
                contador += 1
        return contador

    def contar_libros_prestados(self):
        """Método de colaboración: Cuenta cuántos libros están prestados"""
        contador = 0
        #Recorre la lista de libros y cuenta los prestados
        for libro in self._libros:
            if libro.get_estado().lower() == "no disponible":
                contador += 1
        return contador

        # CARGAR LIBROS AL INICIO
    def menu(self):
        """Menú principal de la biblioteca"""

        #Se inicia primero cargar libros desde el biblio.txt
        self.cargar_libros_desde_archivo()
        
        while True:
            print(self._menu)
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.agregar_libro()
            elif opcion == "2":
                self.eliminar_libro()
            elif opcion == "3":
                self.listar_libros()
            elif opcion == "4":
                self.buscar_libro()
            elif opcion == "5":
                self.marcar_libro_prestado()
            elif opcion == "6":
                self.devolver_libro()
            elif opcion == "7":
                print("Guardando cambios...")
                # GUARDAR LIBROS AL SALIR
                self.guardar_libros_en_archivo()
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")


#Creación clase libro digital heredada de libro
class LibroDigital(Libro):
    def __init__(self, titulo, autor, anio_publicacion, estado, formato):
        super().__init__(titulo, autor, anio_publicacion, estado)
        self.formato = formato

    def __str__(self):
        return f"Título: {self._titulo}, Autor: {self._autor}, Año: {self._anio_publicacion}, Estado: {self._estado}, Formato: {self.formato}"

if __name__ == "__main__":
    #Se crea una instancia de la biblioteca y se inicia el menú
    biblioteca = Biblioteca()
    biblioteca.menu()
