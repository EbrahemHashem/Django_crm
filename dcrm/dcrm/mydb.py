import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1235",
)

# preparing a cursor object
cursorObject = dataBase.cursor()

# Creating a database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS dcrm_db")

