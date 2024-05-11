from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager , login_manager , login_user
app = Flask(__name__ , template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SECRET_KEY'] = '6e8d2fcb509f785bae4734ab'
db = SQLAlchemy(app)
 

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login_page'


from project import routes
from project.models import User


    


