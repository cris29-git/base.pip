import pymysql

# Parámetros de conexión
host = 'localhost:5432/',
user = 'SICTE=S.A.S',
password = 'sicte2023',
database = 'postgresql',

# Conexión a la base de datos
connection = pymysql.connect(
    host= 'localhost:5432/',
    user= 'SICTE=S.A.S',
    password= 'sicte2023',
    database= 'postgresql',
)

try:
    # Crear un cursor
    cursor = connection.cursor()

    # Ejecutar consulta SQL
    sql = 'SELECT * FROM nombre_tabla'
    cursor.execute(sql)

    # Obtener resultados
    results = cursor.fetchall()
    for row in results:
        print(row)

finally:
    # Cerrar cursor y conexión
    cursor.close()
    connection.close()
