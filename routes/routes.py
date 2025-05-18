from flask import render_template, request, redirect, url_for, Blueprint
from models.models import get_db
from flask import abort
from services import stock_alerts

def register_routes(app):
    @app.teardown_appcontext
    def teardown_db(exception):
        from models.models import close_db
        close_db()

    @app.route('/')
    def index():
        pieces = get_db().execute('SELECT rowid, * FROM pieces').fetchall()
        stats = stock_alerts.get_stock_stats()
        avg_cost = stock_alerts.get_average_cost()
        alerts = stock_alerts.get_low_stock_alerts()
        return render_template('index.html', pieces=pieces, stats=stats, avg_cost=avg_cost, alerts=alerts)


    @app.route('/pieces')
    def list_pieces():
        db = get_db()
        pieces = db.execute('SELECT rowid, * FROM pieces').fetchall()
        return render_template('piece_list.html', pieces=pieces)



    @app.route('/pieces/<int:piece_id>/edit', methods=['GET', 'POST'])
    def edit_piece(piece_id):
        db = get_db()
        if request.method == 'POST':
            db.execute('UPDATE pieces SET stock_actuel = ?, stock_minimum = ? WHERE rowid = ?',
                      (request.form['stock_actuel'], request.form['stock_minimum'], piece_id))
            db.commit()
            return redirect(url_for('detail_piece', piece_id=piece_id))
        
        piece = db.execute('SELECT rowid, * FROM pieces WHERE rowid = ?', (piece_id,)).fetchone()
        if piece is None:
            abort(404)
        return render_template('piece_edit.html', piece=piece)

    @app.route('/alerts')
    def alerts():
        db = get_db()
        alerts = db.execute('SELECT rowid, * FROM pieces WHERE stock_actuel <= stock_minimum').fetchall()
        return render_template('alerts.html', alerts=alerts)
    
    @app.route('/pieces/<int:piece_id>')
    def detail_piece(piece_id):
        db = get_db()
        piece = db.execute('SELECT rowid, * FROM pieces WHERE rowid = ?', (piece_id,)).fetchone()
        interventions = db.execute('SELECT * FROM interventions WHERE piece_id = ? ORDER BY date DESC', (piece_id,)).fetchall()
        return render_template('piece_detail.html', piece=piece, interventions=interventions)

    @app.route('/pieces/<int:piece_id>/intervention', methods=['POST'])
    def add_intervention(piece_id):
        type_int = request.form['type']
        commentaire = request.form['commentaire']
        db = get_db()
        db.execute(
            'INSERT INTO interventions (piece_id, type, commentaire) VALUES (?, ?, ?)',
            (piece_id, type_int, commentaire)
        )
        db.commit()
        return redirect(url_for('detail_piece', piece_id=piece_id))