Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import mysql.connector

class MyDatabase:
    def open_connection(self):
        connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="db_cine")
        return connection

    def insert_db(self, pelicula,hora , fecha, idioma):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "INSERT INTO tbl_cartelera(PELICULA,HORA,FECHA,IDIOMA) VALUES (%s,%s,%s,%s)"
        data = (PELICULA,HORA,FECHA,IDIOMA)
        cursor.execute(query,data)
        my_connection.commit()
        my_connection.close()
