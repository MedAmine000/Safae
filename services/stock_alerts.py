from models.models import get_db

def get_low_stock_alerts():
    db = get_db()
    return db.execute(
        'SELECT * FROM pieces WHERE stock_actuel <= stock_minimum'
    ).fetchall()

def get_critical_pieces():
    db = get_db()
    return db.execute(
        'SELECT * FROM pieces WHERE criticite = "Urgente"'
    ).fetchall()

def get_stock_stats():
    db = get_db()
    result = db.execute('''
        SELECT criticite, COUNT(*) as count FROM pieces GROUP BY criticite
    ''').fetchall()
    return {row['criticite']: row['count'] for row in result}

def get_average_cost():
    db = get_db()
    result = db.execute('SELECT AVG(cout_unitaire_eur) as avg_cost FROM pieces').fetchone()
    return result['avg_cost'] if result else 0
