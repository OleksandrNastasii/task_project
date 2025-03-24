from flask import Flask
from app.user_routes import create, delete, update, getuser, getusers
from flask_swagger_ui import get_swaggerui_blueprint
import os
from app.database.database import init_db
from flask import send_from_directory
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{os.getenv("MYSQL_USER")}:{os.getenv("MYSQL_PASSWORD")}@{os.getenv("MYSQL_DATABASE")}:3306/{os.getenv("MYSQL_DATABASE")}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_db()

    SWAGGER_URL = "/api/docs"
    API_URL = "/swagger.json" 

    swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    @app.route("/swagger.json")
    def serve_swagger_json():
        return send_from_directory(os.path.join(os.path.dirname(__file__), "user_routes/swagger"), "swagger.json")

    app.register_blueprint(create)
    app.register_blueprint(update)
    app.register_blueprint(delete)
    app.register_blueprint(getuser)
    app.register_blueprint(getusers)

    return app