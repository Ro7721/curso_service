import mysql.connector

def conectionbb():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user = "root",
            password = "",
            database = "proyecto"
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None