CREATE_RESERVATIONS = '''
    CREATE TABLE IF NOT EXISTS reservations (
        id integer PRIMARY KEY NOT NULL,
        user_id INTEGER FOREIGN KEY REFERENCES users(id),
        projection_id INTEGER FOREIGN KEY REFERENCES projections(id),
        row INTEGER,
        col INTEGER
    );
'''