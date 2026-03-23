import sqlite3
from datetime import datetime, timedelta

def insertar_producto(nombre, stock, vencimiento):
    try:
        # Conectamos a la misma base de datos que usa database.py
        conn = sqlite3.connect('inventario_organico.db')
        cursor = conn.cursor()
        
        # Insertamos el producto
        cursor.execute('''
            INSERT INTO productos (nombre, stock, vencimiento)
            VALUES (?, ?, ?)
        ''', (nombre, stock, vencimiento))
        
        conn.commit()
        conn.close()
        print(f"✅ Producto '{nombre}' añadido con éxito.")
    except Exception as e:
        print(f"❌ Error al insertar: {e}")

if __name__ == "__main__":
    print("--- Cargando Inventario Inicial ---")
    
    # Calculamos fechas dinámicas para probar el informe
    hoy = datetime.now()
    vence_pronto = (hoy + timedelta(days=3)).strftime('%Y-%m-%d')
    vencido = (hoy - timedelta(days=5)).strftime('%Y-%m-%d')
    ok = (hoy + timedelta(days=30)).strftime('%Y-%m-%d')

    # Datos de prueba
    insertar_producto("Tomate Orgánico", 50, vence_pronto)  # Saldrá como PRÓXIMO A VENCER
    insertar_producto("Lechuga Romana", 20, vencido)       # Saldrá como VENCIDO
    insertar_producto("Manzana Roja", 100, ok)             # Saldrá como OK
    insertar_producto("Espinaca Baby", 15, hoy.strftime('%Y-%m-%d')) # Vence hoy
