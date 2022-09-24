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
    item_orders = db.relationship("Order", backref="order_items", lazy=True)


class Order(BaseModel):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)
    contact_id = db.Column(db.Integer, db.ForeignKey("contact.id"), nullable=False)


class Contact(BaseModel):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    first = db.Column(db.String(32), nullable=False)
    last = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(32), nullable=False)
    phone = db.Column(db.String(32), nullable=False)
    contact_orders = db.relationship("Order", backref="order_contacts", lazy=True)
