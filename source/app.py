from flask import Flask, render_template, request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate

from source import controllers
from source.config import Config
from source.models import Hash, Item, Order, db
from source.schemas import (HashResponse, OrderRequest, OrderRequestSchema,
                            OrderResponse)

app = Flask(__name__)
app.config.from_object(Config())
db.init_app(app)
if app.config["MIGRATING"]:
    migrate = Migrate(app, db)
if app.config["ENV"] == "DEV":
    admin = Admin(app)
    admin.add_view(ModelView(Item, db.session))
    admin.add_view(ModelView(Order, db.session))
    admin.add_view(ModelView(Hash, db.session))


@app.route("/", methods=["GET"])
def index() -> str:
    return render_template("index.html")


@app.route("/order", methods=["GET", "POST"])
def order() -> str:
    if request.method == "GET":
        return render_template("order.html")
    req: OrderRequest = OrderRequestSchema().load(request.form.to_dict())
    res: OrderResponse = controllers.add_order(req)
    return render_template("order_response.html", succeeded=res.succeeded)


@app.route("/hashes", methods=["GET"])
def hashes() -> str:
    res: HashResponse = controllers.get_hashes()
    return render_template("hashes.html", hashes=res.hashes)
