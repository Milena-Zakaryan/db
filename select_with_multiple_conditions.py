#SELECT * FROM komanda WHERE gorod = 'City A' AND vuz = 'University X';

@app.route('/teams/filter', methods=['GET'])
def filter_teams():
    gorod = request.args.get('gorod')
    vuz = request.args.get('vuz')
    if not gorod or not vuz:
        return jsonify({"error": "gorod and vuz are required parameters"}), 400
    teams = Team.query.filter_by(gorod=gorod, vuz=vuz).all()
    return jsonify([team.as_dict() for team in teams])


