DROP_TABLE_QUERY = "DROP TABLE IF EXISTS Client"

CREATE_TABLE_QUERY = """
    CREATE TABLE Client (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name CHAR(25) NOT NULL,
        last_name CHAR(25) NOT NULL
    );
"""

ADD_QUERY = "INSERT INTO Client (first_name, last_name) VALUES (?, ?)"
SELECT_ALL_CLIENTS_QUERY = "SELECT * FROM Client"
