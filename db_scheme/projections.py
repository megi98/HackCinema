CREATE_PROJECTIONS = '''
    CREATE TABLE IF NOT EXISTS projections (
        id INTEGER PRIMARY KEY NOT NULL,
        movie_id INTEGER NOT NULL,
        type VARCHAR(5),
        date DATE,
        time VARCHAR(5),
        FOREIGN KEY (movie_id) REFERENCES movies(id)
    );
'''
