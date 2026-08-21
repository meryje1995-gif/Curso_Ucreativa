'''
Mantenimiento en una base de datos XAMPP phpMyAdmin, base zapatería
Tablas: clientes, productos, proveedores y ventas
Programa de reporte general de ventas.
***** Estamos construyendo el reporte general ***
alt + 200-201-205 --> ╚ ╔ ═ ╗
'''
#llamados archivo de sistema
from conectorBD import*
from validarV import*
import math
from datetime import datetime
import subprocess

#función limpiar pantalla
def limpiar():
    subprocess.run("cls", shell=True)

def consultaG():
    cur = cnn.cursor() # crear un cursor para el acceso a la base
    cur.execute("SELECT * FROM ventas") #cursor esta ejecutando el SQL
    datos = cur.fetchall() #con fetchall son todas las filas de la tabla
    if len(datos) != 0:
        for campos in datos:
            print()
            print('*********************************')
            print('** Resgistro de venta número: ', campos[0], '**')
            fecha = campos[1]
            fecha = datetime.strftime(fecha, '%d/%m/%Y')
            print()
            print('Fecha de venta: ',       fecha)
            print('Descripción de venta: ', campos[2])
            print('Precio de venta: ',      campos[3])
            print('Impuesto de venta: ',    campos[4])
            print('Total de venta: ',       campos[5])
            print('Cantidad de venta: ',    campos[6])
            print('Tipo de venta: ',        campos[7])
            print('Cliente de venta: ',     campos[8])
            print('Proveedores de venta: ', campos[9])
    else:
        print()
        print('¡No existen registros en la tabla consultada!')
        print()
    print('______________________________')
    print('** Fin de la consulta general ')
    print('______________________________')
    cur.close() #para cerrar el cursor
