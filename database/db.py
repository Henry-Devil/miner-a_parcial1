import mysql.connector

class Database:
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.cnx = mysql.connector.connect(user=self.user, password=self.password,
                                            host=self.host, database=self.database)
        self.cursor = self.cnx.cursor()
    
    def query(self, query, values=None):
        self.cursor.execute(query, values)
        self.cnx.commit()
        self.cursor.fetchall()  # leer y descartar cualquier resultado sin leer
        return self.cursor.fetchall()

    
    def __del__(self):
        
        self.cursor.fetchall()  # leer y descartar cualquier resultado sin leer
        self.cursor.close()
        self.cnx.close()