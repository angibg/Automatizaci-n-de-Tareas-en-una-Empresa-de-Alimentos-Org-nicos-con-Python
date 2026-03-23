import sqlite3

def insertar_producto(nombre, stock, vencimiento):
    conn = sqlite3.connect('inventario_organico.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO productos (nombre, stock, vencimiento)
        VALUES (?, ?, ?)
    ''', (nombre, stock, vencimiento))
    conn.commit()
    conn.close()

# Insertando ejemplos orgánicos
insertar_producto("Tomate Cherry Orgánico", 50, "2026-03-25")
insertar_producto("Lechuga Hidropónica", 20, "2026-03-18")
insertar_producto("Manzana Gala", 100, "2026-04-10")

print("Datos insertados correctamente.")

