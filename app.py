from flask import Flask, render_template
from dotenv import load_dotenv
from databases.db import db, init_db
from models.guarderia import Guarderia
from controllers.controller_animales import guarderia_bp

import os

load_dotenv()
app = Flask(__name__, template_folder="views")

# Para uso local
# app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# Para uso web
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://root:KPcLrzsEngDJeXHahVjDdPwNKYcMzGEq@autorack.proxy.rlwy.net:25862/railway"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
init_db(app)
app.register_blueprint(guarderia_bp)


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':    
    app.run(debug=True)
    