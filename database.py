import sqlite3
def conectar():
     return sqlite3.connect("invenario.db")
def obtener_productos():
    conn= conectar()
    cursor=conn.cursor()
    cursor.execute("SELECT id , nombre , stock ,vencimiento FROM productos")
    datos = cursor.fetchall()
    conn.close()
    return datos
def actualizar_vencimiento(id_producto,nueva_fecha):
    conn= conectar()
    cursor=conn.cursor()
    cursor.execute("UPDATE productos SET vencimiento=? WHERE id=?", (nueva_fecha, id_producto)
                   )
    conn.commit()
    conn.close()

