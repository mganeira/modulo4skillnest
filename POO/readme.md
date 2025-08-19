Sistema de Manejo de Inventario CSV
Un sistema de gestión de inventario simple y eficiente desarrollado en Python que utiliza archivos CSV para el almacenamiento de datos.
Características

Gestión completa de productos (CRUD: Crear, Leer, Actualizar, Eliminar)
Manejo automático de archivos CSV con encabezados persistentes
Búsqueda de productos por nombre
Sistema de respaldos automáticos con marcas de tiempo
Validación de entrada y manejo robusto de errores
Información detallada del archivo (tamaño, fecha de modificación)
Uso
Menú Principal
Al ejecutar el programa, verás un menú con las siguientes opciones:
1: Ver el inventario
2: Añadir texto al inventario sobreescribiendo
3: Añadir texto al inventario nuevo sin sobreescribir
4: Modificar productos existentes en el inventario
5: Obtener atributos del archivo
6: Leer un producto específico
7: Eliminar un producto
8: Hacer backup
9: Cerrar archivos
Funcionalidades Detalladas
Opción 1: Ver Inventario
Muestra todo el contenido del archivo CSV de inventario.
Opción 2: Sobreescribir Inventario
Reemplaza completamente el contenido del inventario manteniendo los encabezados.

Formato de entrada: Producto1,10.50,5,M
Los encabezados se preservan automáticamente

Opción 3: Añadir al Inventario
Agrega nuevos productos sin eliminar los existentes.

Formato de entrada: Mismo que la opción 2

Opción 4: Modificar Producto
Busca un producto por nombre y permite editar sus campos individualmente.
Opción 5: Información del Archivo
Muestra metadatos del archivo: nombre, tamaño en bytes y fecha de última modificación.
Opción 6: Buscar Producto
Busca productos por nombre (búsqueda parcial, no sensible a mayúsculas).
Opción 7: Eliminar Producto
Elimina un producto específico del inventario con confirmación de seguridad.
Opción 8: Crear Backup
Genera una copia de seguridad del inventario en la carpeta backups/ con timestamp.
Opción 9: Salir
Cierra el programa de forma segura.
Estructura de Archivos
proyecto/
├── inventario.py          # Archivo principal del programa
├── inventario.csv         # Archivo de datos (se crea automáticamente)
└── backups/              # Carpeta de respaldos (se crea automáticamente)
    ├── inventario_backup_20250818_143022.csv
    └── inventario_backup_20250818_150145.csv
Formato de Datos
El sistema utiliza el siguiente formato de encabezados:
NombrePrecioCantidadTallaCamiseta15.9910LPantalón29.505M
Ejemplo de CSV generado:
csvNombre,Precio,Cantidad,Talla
Camiseta,15.99,10,L
Pantalón,29.50,5,M
Zapatos,45.00,3,42
Características Técnicas
Programación Orientada a Objetos

Clase principal: ManejoInventario
Encapsulación: Métodos específicos para cada funcionalidad
Atributos de instancia: Configuración centralizada

Manejo de Archivos

Context managers: Uso de with open() para manejo seguro de archivos
Encoding UTF-8: Soporte completo para caracteres especiales
Modos de apertura:

'r': Lectura
'w': Escritura (sobrescribe)
'a': Anexar (añade al final)



Detección Inteligente de Encabezados
El sistema detecta automáticamente si un archivo CSV tiene encabezados analizando la primera fila:

Si el segundo campo es numérico → Primera fila son datos
Si el segundo campo no es numérico → Primera fila son encabezados

Consideraciones Importantes

Respaldos automáticos: Se recomienda usar la opción 8 antes de realizar cambios importantes
Formato de entrada: Los datos deben separarse por comas sin espacios adicionales
Nombres únicos: El sistema busca productos por nombre exacto para editar/eliminar
Validación: El programa valida la entrada numérica del menú

Manejo de Errores
El sistema incluye manejo robusto de errores para:

Archivos no encontrados
Formato de datos incorrecto
Problemas de permisos de archivo
Entrada de usuario inválida

Funciones Principales
Clase ManejoInventario

__init__(): Inicializa la clase con configuraciones por defecto
inicializar_archivo_con_encabezados(): Crea el archivo CSV con encabezados si no existe
mostrar_menu(): Muestra el menú y valida la entrada del usuario
ver_inventario(): Lee y muestra el contenido completo del inventario
reemplazar_info(): Sobrescribe el inventario manteniendo encabezados
añadir_texto(): Añade productos al inventario existente
editar_producto(): Modifica productos existentes
eliminar_producto(): Elimina productos con confirmación
buscar_producto(): Busca productos por nombre
obtener_atributos_archivo(): Muestra información del archivo
crear_backup(): Crea copias de seguridad
ejecutar(): Función principal que controla el flujo del programa

Contribución
Este proyecto fue desarrollado como parte de un ejercicio académico para el Bootcamp Python Trainee de Skillnest para aprender:

Manipulación de archivos CSV en Python
Programación orientada a objetos
Manejo de excepciones
Interfaces de usuario por consola


Desarrollado para fines educativos y de aprendizaje de Python.
