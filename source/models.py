from datetime import datetime
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


class Item(BaseModel):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    size = db.Column(db.Enum(Size), nullable=False)
    inventory = db.Column(db.Integer, nullable=False)
    item_orders = db.relationship("Order", backref="order_items", lazy=True)


class Order(BaseModel):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    first = db.Column(db.String(32), nullable=False)
    last = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(32), nullable=False)
    phone = db.Column(db.String(32), nullable=False)
    fulfilled = db.Column(db.Boolean, default=False, nullable=False)
    hash = db.Column(db.String(64))
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)
