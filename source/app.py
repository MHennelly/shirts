import config
from flask import Flask
from models import Item, Order, db

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
db.init_app(app)


@app.route("/")
def index():
    return Item.query.all(), Order.query.all()
