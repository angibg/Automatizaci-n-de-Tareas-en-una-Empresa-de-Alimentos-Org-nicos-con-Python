import database
from datetime import datetime, timedelta

def generar_informe_detallado():
    try:
        productos = database.obtener_inventario()
        fecha_actual = datetime.now()
        umbral_alerta = timedelta(days=7)  # Alerta para productos que vencen en una semana

        print(f"--- INFORME DE INVENTARIO AL {fecha_actual.strftime('%d/%m/%Y')} ---")
        print(f"{'Producto':<20} | {'Stock':<8} | {'Vencimiento':<12} | {'Estado'}")
        print("-" * 60)

        for producto in productos:
            # Convertir string de fecha a objeto datetime para comparar
            fecha_vencimiento = datetime.strptime(producto['vencimiento'], '%Y-%m-%d')
            
            # Determinar estado
            if fecha_vencimiento < fecha_actual:
                estado = "⚠️ VENCIDO"
            elif fecha_vencimiento <= fecha_actual + umbral_alerta:
                estado = "⏳ PRÓXIMO A VENCER"
            else:
                estado = "✅ OK"

            print(f"{producto['nombre']:<20} | {producto['stock']:<8} | {producto['vencimiento']:<12} | {estado}")

    except Exception as e:
        print(f"Error al generar el informe: {e}")

if __name__ == "__main__":
    generar_informe_detallado()
