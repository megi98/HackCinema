CREATE_MOVIES = '''
    CREATE TABLE IF NOT EXISTS movies (
        id integer PRIMARY KEY NOT NULL,
        name varchar(100) UNIQUE,
        rating INTEGER
    );
'''