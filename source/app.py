from config import DevelopmentConfig
from flask import Flask
from flask_migrate import Migrate
from models import Item, Order, db

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    return Item.query.all(), Order.query.all()
