@app.route('/teams', methods=['GET'])

def get_teams():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    teams = Komanda.query.paginate(page, per_page, False)  
    result = {
        'teams': [team.as_dict() for team in teams.items],
        'total_pages': teams.pages,
        'current_page': teams.page,
        'has_next': teams.has_next,
        'has_prev': teams.has_prev
    }
    return jsonify(result)
