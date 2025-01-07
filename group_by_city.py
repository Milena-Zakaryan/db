#SELECT mesto, COUNT(*) AS game_count
#FROM igra
#GROUP BY mesto;


@app.route('/games/group-by-city', methods=['GET'])
def group_games_by_city():
    results = db.session.execute("""
        SELECT mesto, COUNT(*) AS game_count
        FROM igra
        GROUP BY mesto
    """).fetchall()
    return jsonify([dict(row) for row in results])
