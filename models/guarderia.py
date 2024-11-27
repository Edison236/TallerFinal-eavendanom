from databases.db import db

class Guarderia(db.Model):
    __tablename__ = 'animales'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    type = db.Column(db.String(50), nullable = False)
    breed = db.Column(db.String(50), nullable = False)
    age = db.Column(db.String(50), nullable = False)
    sound = db.Column(db.String(50), nullable = False)

def insert_animals():
    if not Guarderia.query.first():
        guarderia = [
            Guarderia(name = 'felix',type = 'Gato',breed = 'Birmano',age = '5',sound = 'Miaow'),
            Guarderia(name = 'Teo',type = 'Perro',breed = 'Golden',age = '1',sound = 'Guau'),
            Guarderia(name = 'Ares',type = 'Hurón',breed = 'Bull',age = '2',sound = 'Tsss'),
            Guarderia(name = 'Boa cola roja',type = 'Boa',breed = '',age = '4',sound = 'Eek Eek'),
        ]
        db.session.bulk_save_objects(guarderia)  # Inserta múltiples registros
        db.session.commit()  # Confirma los cambios