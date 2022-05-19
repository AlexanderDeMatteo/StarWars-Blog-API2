from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Personajes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=False, nullable=False)
    clase = db.Column(db.String(120), unique=False, nullable=False)
    faccion = db.Column(db.String(200), unique=False, nullable=False)
    raza = db.Column(db.String(200), unique=False, nullable=False)

    def __repr__(self):
        return '<Personaje %r>' % self.username

    def serialize(self):
        return {
            "nombre": self.nombre,
            "clase": self.clase,
            "faccion": self.faccion,
            "raza": self.raza,
        }

class Planetas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    region = db.Column(db.String(120), unique=False, nullable=False)
    sistema = db.Column(db.String(200), unique=False, nullable=False)
    especie_nativa = db.Column(db.String(200), unique=False, nullable=False)

    def __repr__(self):
        return '<Planetas %r>' % self.username

    def serialize(self):
        return {
            "nombre": self.nombre,
            "region": self.region,
            "sistema": self.sistema,
            "especie_nativa": self.especie_nativa,
        }