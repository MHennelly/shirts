from config import DevelopmentConfig
from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate
from models import Contact, Item, Order, db

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate = Migrate(app, db)
if app.config.get("STAGE") == "DEV":
    admin = Admin(app)
    admin.add_view(ModelView(Item, db.session))
    admin.add_view(ModelView(Order, db.session))
    admin.add_view(ModelView(Contact, db.session))


@app.route("/")
def index():
    return render_template("home.html")
