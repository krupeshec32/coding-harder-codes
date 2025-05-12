from flask import Flask, jsonify
import mysql.connector
import os


class TestDBConnection:
    # Dh12@ruti
    # MySQL configuration from environment variables
    def __init__(self):
        self.db_config = {
            'user': 'root',
            'password': 'Dh12@ruti',
            'host': '127.0.0.1',
            'database': 'baps',
            'port': 3306
        }

    def get_data(self):
        try:
            # Connect to MySQL
            connection = mysql.connector.connect(
                user=self.db_config['user'],
                password=self.db_config['password'],
                host=self.db_config['host'],
                database=self.db_config['database'],
                port=self.db_config['port']
            )
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM MIS_ID_LOOKUP")
            rows = cursor.fetchall()
            return jsonify(rows), 200
        except mysql.connector.Error as err:
            print(str(err))


test = TestDBConnection()
test.get_data()
