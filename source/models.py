from enum import Enum, auto

from flask_sqlalchemy import DeclarativeMeta, SQLAlchemy

db = SQLAlchemy()
BaseModel: DeclarativeMeta = db.Model


class Size(Enum):
    XS = auto()
    S = auto()
    M = auto()
    L = auto()
    XL = auto()


class State(Enum):
    CA = auto()


class Item(BaseModel):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    size = db.Column(db.Enum(Size))
    inventory = db.Column(db.Integer)
    orders = db.relationship("Order", backref="order", lazy=True)


class Order(BaseModel):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    address1 = db.Column(db.String(32), nullable=False)
    address2 = db.Column(db.String(32))
    city = db.Column(db.String(32), nullable=False)
    state = db.Column(db.Enum(State), nullable=False)
    postal_code = db.Column(db.String(16), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)
