import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
	user = 'root',
	passwd = 'shreyas'
)

cursorobject = dataBase.cursor()

cursorobject.execute("CREATE DATABASE CRM_DB")