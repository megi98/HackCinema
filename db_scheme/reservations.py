CREATE_RESERVATIONS = '''
    CREATE TABLE IF NOT EXISTS reservations (
        id integer PRIMARY KEY NOT NULL,
        user_id INTEGER,
        projection_id INTEGER,
        row INTEGER,
        col INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (projection_id) REFERENCES projections(id) 
    );
'''
