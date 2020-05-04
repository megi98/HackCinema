CREATE_PROJECTIONS = '''
    CREATE TABLE IF NOT EXISTS projections (
        id integer PRIMARY KEY NOT NULL,
        movie_id FOREIGN KEY NOT NULL REFERENCES movies(id),
        type VARCHAR(5),
        date DATE,
        time VARCHAR(5)
    );
'''