import mysql.connector
from mysql.connector import errorcode

con = mysql.connector.connect(host='localhost', database='formulario', user='root', password='')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ", db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchmany()

    print("Conectado ao banco de dados", linha)
elif not con.is_connected():
    print('Não foi possível se conectar no banco de dados.')
