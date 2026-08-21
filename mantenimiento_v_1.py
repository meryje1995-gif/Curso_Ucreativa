''' Mantenimiento en una base de datos Xampp, base labuenataza Tabla:ventas
Version 1
**** vamos a implementar una inserción de venta *****
alt - 201 ╔
    - 187 ╗
    - 200 ╚
    - 188 ╝
    - 186 ║
    - 205 ═
    '''
'''
Menú con Case
'''
# llamados de archivo de sistema
from conectorBD import *       # importar el archivo de conexión
from validarV import *         # importa el archivo de validación
from reporteTotalBD import *   # importa el reporte total de ventas
from datetime import datetime  # archivo interno al cual llamo una función
import mysql.connector         # llamado al conector
import math 
import subprocess

#función de saludo
def saludo(nombre):
    if nombre != '':
        print('Bienvenido(a): ', nombre)
    else:
        print('Bienvenido(a), la próxima vez el nombre por favor')
    return()
#función de despedida
def despedida(nombre):
    print("Fue un gusto servirte ", nombre)
    return()

#función limpiar pantalla
def limpiar():
    subprocess.run("cls", shell=True)

# función encabezado
def encabezado():
    fecha = datetime.now()
    print('****************')
    print(f'{fecha.day}-{fecha.month}-{fecha.year}')
    print('****************')
    titulo = '''
    ╔═════════════════════════════════════════════╗
    ║ ******** SISTEMA DE MANTENIMIENTO ********* ║
    ║                                             ║
    ║          **** Base de datos ****            ║
    ║                                             ║ 
    ║          ****Python - MySQL v.1 ****        ║
    ║                                             ║
    ╚═════════════════════════════════════════════╝
'''
    print(titulo)
    return

#función menú
def menu():
    opciones = ('''
    ╔═══════════════════════════════════════════════════╗
    ║       ********    MENÚ DE OPCIONES   ******       ║
    ║       *                                   *       ║
    ║       *               VENTAS              *       ║
    ║       *************************************       ║
    ║                                                   ║            
    ║           1: => Insertar    Venta   ****          ║
    ║                                                   ║                
    ║           2: => Consultar   Venta   ****          ║
    ║                                                   ║
    ║           3: => Actualizar  Venta   ****          ║
    ║                                                   ║
    ║           4: => Reporte   General   ****          ║
    ║                                                   ║            
    ║           5: => Borrar      Venta   ****          ║
    ║                                                   ║
    ║           6: =>   SALIR             ****          ║
    ║                                                   ║
    ╚═══════════════════════════════════════════════════╝
    '''
    )
    print(opciones)  
    return

#función insertar venta
def insertarVenta():
    limpiar() #clear
    print('***      Ingreso de Venta     ***')
    print('*********************************')
    print('**  Digite datos de la venta   **')
    #captura de datos
    fecha = input('Digite la fecha:  ejemplo 01/01/2026 ')
    fechaB = datetime.strptime(fecha, '%d/%m/%Y') #para capturar fecha en español
    desc = input('Digite la descripción: ')
    precio = input('Digite el precio: ') #validar como decimal
    impuesto = input('Digite el impuesto: ') #validar como decimal
    total = input('Digite el total: ') #validar como decimal
    cantidad1 = input('Digite la cantidad: ') #validar como entero
    cantidad = validar(cantidad1, 1)
    #cantidad = validar(cantidad1, 2)
    pago1 = input('Digite la forma de pago: ')
    pago = validar(pago1, 2)
    cliente = input('Digite el cliente: ')
    producto = input('Digite el producto: ')  
    #proceso para insertar datos
    cur = cnn.cursor()
    sql = ('''INSERT INTO `ventas`(`ventId`, `ventFecha`, `ventDesc`,
    `ventPrecio`, `ventImpue`, `ventTotal`, `ventCant`, `ventPago`, `idCliente`, `idProductos`)
    VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format('', fechaB, desc, precio, impuesto,
        total, cantidad, pago, cliente, producto))
    cur.execute(sql)
    cnn.commit()
    cur.close()    
    return

#función consulta de venta
def consultarVenta():
    limpiar() #clear
    print('***      Consulta de Venta     ***')
    print('*********************************')
    consulta = input('Digite el código de venta: ')
    cur = cnn.cursor()  #crear un curso para acceso a la base de datos
    cur.execute('''SELECT * FROM `ventas` WHERE `ventId` = {}'''.format(consulta))
    datos_db = cur.fetchall() #con fetcha all trae todos los datos de fila o tupla
    if len(datos_db) != 0:
        for campos in datos_db:
            print('** Registro de Ventas número: ',campos[0])
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
        print('¡Número de venta no encontrada!')
        print()
    cur.close()
    return()

#función actualizar venta
def actualizarVenta():
    limpiar() #clear
    print('***      Actualizar de Venta     ***')
    print('************************************')
    consulta = input('Digite el código de venta: ')
    cur = cnn.cursor()  #crear un curso para acceso a la base de datos
    cur.execute('''SELECT * FROM `ventas` WHERE `ventId` = {}'''.format(consulta))
    datos_db = cur.fetchall() #con fetcha all trae todos los datos de fila o tupla
    if len(datos_db) != 0:
        for campos in datos_db:
            print('** Registro de Ventas número: ',campos[0])
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

        respuesta = input('Seguro que deseas actualizar el registro: S/N ')
        respuesta = respuesta.upper()
        if respuesta == 'S':
            print('** Registro de Ventas número: ',campos[0])
            print('****************************************')
            #captura de datos
            fecha = input('Digite la fecha:  ejemplo 01/01/2026 ')
            fechaB = datetime.strptime(fecha, '%d/%m/%Y') #para capturar fecha en español
            desc = input('Digite la descripción: ')
            precio = input('Digite el precio: ')
            impuesto = input('Digte el impuesto: ')
            total = input('Digite el total: ')
            cantidad = input('Digite la cantidad: ')
            pago = input('Digite la forma de pago: ')
            cliente = input('Digite el cliente: ')
            producto = input('Digite el producto: ')  
            cur = cnn.cursor()
            sql = '''UPDATE `ventas` SET `ventFecha`='{}',
                `ventDesc`='{}',`ventPrecio`='{}',`ventImpue`='{}',
                `ventTotal`='{}',`ventCant`='{}',`ventPago`='{}',
                `idCliente`='{}',`idProductos`='{}' WHERE `ventId` = {}'''.format(fechaB, desc, precio, impuesto,
                total, cantidad, pago, cliente, producto, consulta)
            cur.execute(sql)
            cnn.commit()
            cur.close()
            print(f'Registro de ventas #{campos[0]} has sido actualizado con éxito!')
        else:
            print('¡No se actulizó ningún registro!')
    else:
        print()
        print('¡Número de venta no encontrada!')
        print()
    return

#función borrar datos
def borrarVenta():
    factura = input('Digite el número de pedido que desea borrar: ')
    cur = cnn.cursor()  #crear un curso para acceso a la base de datos
    cur.execute('''SELECT * FROM `ventas` WHERE `ventId` = {}'''.format(factura))
    datos_db = cur.fetchall() #con fetcha all trae todos los datos de fila o tupla
    if len(datos_db) != 0:
        for campos in datos_db:
            print('** Registro de Ventas número: ',campos[0])
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
        respuesta = input('¿Seguro que deseas eliminar el registro: S/N? ')
        respuesta = respuesta.upper()
        if respuesta == 'S':
            cur.execute('''DELETE FROM `ventas` WHERE `ventId` = {}'''.format(factura))
            cnn.commit()
            cur.close()
            print('¡Registro de venta ha sido eliminado exitosamente!')
        else:
            print('¡No se elimino ningún registro!')
    else:
        print()
        print('¡Archivo no encontrado!')    
    return()

#********************** Principal o MAIN  *************************
def main():
    cantidad, cliente, proveedores = int, int, int
    fecha, ventId, desc, pago = str, str, str, str
    precio, impuesto, total = float, float, float
    continuar = True
   
    while continuar:
        nombre = input('Digite su nombre: ')
        saludo(nombre)
        encabezado()
        menu()
        opc1 = input('Seleccione una opción: ')
        opc = validar(opc1, 1)
        match opc1:
            case "1":
                insertarVenta()
            case "2":
                consultarVenta()
            case "3":
                actualizarVenta()
            case "4":
                consultaG()
            case "5":
                borrarVenta()
            case "6":
                cnn.close() #para cerrar la conexión de la base de datos
                break
            case _:
                print('Opción no es válida...')
        input('Digite cualquier tecla para continuar...')
    print('Estamos para servirte, Muchas gracias.')
    despedida(nombre)

if __name__ == '__main__':
        main()
