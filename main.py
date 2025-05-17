import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # DON'T CHANGE THIS !!!

from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import requests
import json
from datetime import datetime

# Inicialização do app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta_do_site_lite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site_lite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/uploads')

# Inicialização do banco de dados
db = SQLAlchemy(app)

# Inicialização do login manager
login_manager = LoginManager(app)
login_manager.login_view = 'admin_login'

# Importação de rotas e modelos
from src.routes.main_routes import main_bp
from src.routes.admin_routes import admin_bp
from src.routes.payment_routes import payment_bp

# Registro dos blueprints
app.register_blueprint(main_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(payment_bp, url_prefix='/payment')

# Rota principal
@app.route('/')
def index():
    return redirect(url_for('main.home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
