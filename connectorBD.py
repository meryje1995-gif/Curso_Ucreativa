import mysql.connector

try:
    cnn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='labuenataza'
    )
    #print('La conexión con la base fue exitosa')
except:
    print('No funcionó la conexión con la base de datos')
    
    
