from comunidadesenai import app, database
from comunidadesenai.models import Usuario


with app.app_context():
    database.drop_all()