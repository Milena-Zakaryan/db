#SELECT igra.nazvanie AS igra_name, komanda.nazvanie AS komanda_name, rezultati.balli 
#FROM rezultati
#JOIN komanda ON rezultati.komanda_id = komanda.id
#JOIN igra ON rezultati.igra_id = igra.id;


@app.route('/results/with-details', methods=['GET'])
def results_with_details():
    results = db.session.execute("""
        SELECT igra.nazvanie AS igra_name, komanda.nazvanie AS komanda_name, rezultati.balli 
        FROM rezultati
        JOIN komanda ON rezultati.komanda_id = komanda.id
        JOIN igra ON rezultati.igra_id = igra.id
    """).fetchall()
    return jsonify([dict(row) for row in results])
