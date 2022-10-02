from flask import Flask, render_template, request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate
from marshmallow.schema import ValidationError

from source import controllers
from source.config import Config, logger
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
    item = request.args.get("item")
    if request.method == "GET":
        return (
            render_template("order_form.html", item=item)
            if item
            else render_template(
                "store.html",
                regular=Item.query.filter_by(limited=False).all(),
                limited=Item.query.filter_by(limited=True).all(),
            )
        )
    try:
        req: OrderRequest = OrderRequestSchema().load(
            {"item": item, "phone": request.form.get("phone")}
        )
    except ValidationError as e:
        logger.info(e)
        return render_template("order_error.html")
    res: OrderResponse = controllers.add_order(req)
    return render_template("order_response.html", succeeded=res.succeeded)


@app.route("/hashes", methods=["GET"])
def hashes() -> str:
    res: HashResponse = controllers.get_hashes()
    return render_template("hashes.html", hashes=res.hashes)
