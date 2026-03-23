import database
from database import datatime
import  pandas  as pd
def analizar_inventario():
    productos = database.obtener_productos()
    hoy  = datatime.today()

reporte=[]

for producto in productos:
    id_p,nombre,stock,vencimiento=producto
    # estado de stock
    if stock= 0
estado _stock="sin stock"
elif stock <=10:
estado _stock="bajo"
else:
estado_stock ="ok"
# estado de vencimiento
fecha_vencimiento= datatime.strptime(vencimiento,"%Y-%m-%d")

