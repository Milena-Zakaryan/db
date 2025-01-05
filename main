from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/your_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Komanda(db.Model):
    __tablename__ = 'komanda'
    id = db.Column(db.Integer, primary_key=True)
    nazvanie = db.Column(db.String(50))
    vuz = db.Column(db.String(100))
    gorod = db.Column(db.String(50), nullable=False)

class Igra(db.Model):
    __tablename__ = 'igra'
    id = db.Column(db.Integer, primary_key=True)
    nazvanie = db.Column(db.String(50), nullable=False)
    liga = db.Column(db.Integer)
    data = db.Column(db.Date)
    mesto = db.Column(db.String(50))

class Rezultati(db.Model):
    __tablename__ = 'rezultati'
    id = db.Column(db.Integer, primary_key=True)
    mesto = db.Column(db.Integer)
    balli = db.Column(db.BigInteger)
    vixod_v_sled_etap = db.Column(db.String(20), nullable=False)
    komanda_id = db.Column(db.Integer, db.ForeignKey('komanda.id'))
    igra_id = db.Column(db.Integer, db.ForeignKey('igra.id'))

#API
@app.route('/komanda', methods=['GET'])
def get_komandy():
    komandy = Komanda.query.all()
    result = [{"id": k.id, "nazvanie": k.nazvanie, "vuz": k.vuz, "gorod": k.gorod} for k in komandy]
    return jsonify(result)

@app.route('/igra', methods=['POST'])
def add_igra():
    data = request.json
    new_igra = Igra(
        nazvanie=data['nazvanie'],
        liga=data.get('liga'),
        data=data.get('data'),
        mesto=data.get('mesto')
    )
    db.session.add(new_igra)
    db.session.commit()
    return jsonify({"message": "Igra added successfully"}), 201

@app.route('/rezultati/<int:id>', methods=['DELETE'])
def delete_rezultat(id):
    rezultat = Rezultati.query.get(id)
    if not rezultat:
        return jsonify({"message": "Rezultat not found"}), 404
    db.session.delete(rezultat)
    db.session.commit()
    return jsonify({"message": "Rezultat deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
