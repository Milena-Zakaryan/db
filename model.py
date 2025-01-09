from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Komanda(db.Model):
    __tablename__ = 'komanda'
    id = db.Column(db.Integer, primary_key=True)
    nazvanie = db.Column(db.String(50))
    vuz = db.Column(db.String(100))
    gorod = db.Column(db.String(50), nullable=False)
    dop_info = db.Column(db.JSONB)
    def __init__(self, nazvanie, vuz, gorod, dop_info=None):
        self.nazvanie = nazvanie
        self.vuz = vuz
        self.gorod = gorod
        self.dop_info = dop_info
    def __repr__(self):
        return f'<Komanda {self.nazvanie}>'

# new_team = Komanda(nazvanie='Team A', vuz='University X', gorod='City A', dop_info={"history": "Founded in 2005"})
# db.session.add(new_team)
# db.session.commit()

# teams = Komanda.query.all()
# teams_in_city = Komanda.query.filter_by(gorod='City A').all()
