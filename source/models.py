from datetime import datetime

from flask_sqlalchemy import DeclarativeMeta, SQLAlchemy

db = SQLAlchemy()
BaseModel: DeclarativeMeta = db.Model


class Item(BaseModel):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(64))
    limited = db.Column(db.Boolean, nullable=False)
    item_hashes = db.relationship("Hash", backref="item", lazy=True)
    item_orders = db.relationship("Order", backref="item", lazy=True)


class Hash(BaseModel):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    value = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)
    hash_order = db.relationship("Order", backref="hash", lazy=True)


class Order(BaseModel):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)
    hash_id = db.Column(db.Integer, db.ForeignKey("hash.id"))
