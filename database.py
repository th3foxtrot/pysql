import mysql.connector

config = {
    'user': 'root',
    'password': '121212aa',
    'host': 'localhost'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()