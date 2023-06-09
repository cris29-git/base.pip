import pymysql

# Parámetros de conexión
host = 'localhost'
user = 'nombre_usuario'
password = 'contraseña'
database = 'nombre_base_de_datos'

# Conexión a la base de datos
connection = pymysql.connect(host=host, user=user, password=password, database=database)

# Crear un cursor
cursor = connection.cursor()

# Ejecutar consulta SQL
sql = 'SELECT * FROM nombre_tabla'
cursor.execute(sql)

# Obtener resultados
results = cursor.fetchall()
for row in results:
    print(row)

# Cerrar cursor y conexión
cursor.close()
connection.close()
