@app.route('/teams/sorted', methods=['GET'])
def get_sorted_teams():
    sort_field = request.args.get('sort_field', 'nazvanie')
    sort_order = request.args.get('sort_order', 'asc')
    query = Team.query.order_by(getattr(Team, sort_field).asc() if sort_order == 'asc' else getattr(Team, sort_field).desc())
    teams = query.all()
    return jsonify([team.as_dict() for team in teams])
