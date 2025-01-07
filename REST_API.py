from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'
db = SQLAlchemy(app)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazvanie = db.Column(db.String(50))
    vuz = db.Column(db.String(100))
    gorod = db.Column(db.String(50), nullable=False)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazvanie = db.Column(db.String(50), nullable=False)
    liga = db.Column(db.Integer)
    data = db.Column(db.Date)
    mesto = db.Column(db.String(50))

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mesto = db.Column(db.Integer)
    balli = db.Column(db.BigInteger)
    vixod_v_sled_etap = db.Column(db.String(20), nullable=False)
    komanda_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    igra_id = db.Column(db.Integer, db.ForeignKey('game.id'))

@app.route('/teams', methods=['GET', 'POST'])
def teams():
    if request.method == 'GET':
        all_teams = Team.query.all()
        return jsonify([team.as_dict() for team in all_teams])
    elif request.method == 'POST':
        data = request.get_json()
        new_team = Team(nazvanie=data['nazvanie'], vuz=data['vuz'], gorod=data['gorod'])
        db.session.add(new_team)
        db.session.commit()
        return jsonify(new_team.as_dict()), 201

@app.route('/games', methods=['GET', 'POST'])
def games():
    if request.method == 'GET':
        all_games = Game.query.all()
        return jsonify([game.as_dict() for game in all_games])
    elif request.method == 'POST':
        data = request.get_json()
        new_game = Game(nazvanie=data['nazvanie'], liga=data['liga'], data=data['data'], mesto=data['mesto'])
        db.session.add(new_game)
        db.session.commit()
        return jsonify(new_game.as_dict()), 201

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'GET':
        all_results = Result.query.all()
        return jsonify([result.as_dict() for result in all_results])
    elif request.method == 'POST':
        data = request.get_json()
        new_result = Result(mesto=data['mesto'], balli=data['balli'], vixod_v_sled_etap=data['vixod_v_sled_etap'], komanda_id=data['komanda_id'], igra_id=data['igra_id'])
        db.session.add(new_result)
        db.session.commit()
        return jsonify(new_result.as_dict()), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
