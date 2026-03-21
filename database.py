<<<<<<< HEAD
import sqlite3

def conectar():
    """Establece conexión con el archivo de base de datos."""
    return sqlite3.connect('inventario_organico.db')

def inicializar_db():
    """Crea la tabla de productos si no existe."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            stock INTEGER NOT NULL,
            vencimiento DATE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def obtener_inventario():
    """Consulta la base de datos y devuelve una lista de diccionarios."""
    conn = conectar()
    # Esto permite acceder a las columnas por nombre (producto['nombre'])
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor()
    
    cursor.execute("SELECT nombre, stock, vencimiento FROM productos")
    filas = cursor.fetchall()
    
    # Convertimos el objeto Row a una lista de diccionarios
    inventario = [dict(fila) for fila in filas]
    
    conn.close()
    return inventario

# Inicializar la base de datos al importar el módulo
inicializar_db()
=======
# database.py
>>>>>>> a21880a (Initial commit)
