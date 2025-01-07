--UPDATE rezultati
--SET balli = balli + 10
--WHERE mesto = 1 AND vixod_v_sled_etap = 'yes';


@app.route('/results/update-scores', methods=['PUT'])
def update_scores():
    mesto = request.args.get('mesto', type=int, default=1)
    results = db.session.execute("""
        UPDATE rezultati
        SET balli = balli + 10
        WHERE mesto = :mesto AND vixod_v_sled_etap = 'yes'
        RETURNING id, balli;
    """, {'mesto': mesto}).fetchall()
    db.session.commit()
    return jsonify([dict(row) for row in results])
