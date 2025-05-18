import sqlite3
from flask import g, current_app

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_intervention_table():
    db = get_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS interventions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            piece_id INTEGER,
            type TEXT,
            commentaire TEXT,
            date TEXT DEFAULT CURRENT_DATE
        )
    ''')
    db.commit()