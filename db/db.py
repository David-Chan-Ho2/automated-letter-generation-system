import sqlite3
from . import queries
from helpers import dict2tuples

class DB:
    
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.drop_table()
    
    def drop_table(self):
        self.cur.execute(queries.DROP_TABLE_QUERY)
    
    def create_table(self):
        self.cur.execute(queries.CREATE_TABLE_QUERY)
        
    def add_table(self, client):
        self.cur.execute(queries.ADD_QUERY,  (client['first_name'], client['last_name']))
        self.conn.commit()
        
    def add_many(self, clients):
        self.cur.executemany(queries.ADD_QUERY, clients)
        self.conn.commit()
    
    def seed(self, clients):
        formatted_clients = dict2tuples(clients)
        self.add_many(formatted_clients)
        
    def close(self):
        self.conn.close()