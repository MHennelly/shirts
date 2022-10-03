from source.config import logger
from source.models import Hash, Item, Order, db
from source.schemas import (HashResponse, OrderRequest, OrderResponse,
                            StoreResponse)


def add_order(req: OrderRequest) -> OrderResponse:
    try:
        item = Item.query.filter_by(name=req.item).first()
        if not item:
            raise ValueError("Item Doesn't Exist")
        if item.limited and any(order.hash_id for order in item.item_orders):
            raise ValueError("Limited Item Already Sold")
        order = Order(phone=req.phone, item_id=item.id)
        db.session.add(order)
        db.session.commit()
    except ValueError as e:
        logger.info(e)
        return OrderResponse(succeeded=False)
    return OrderResponse(succeeded=True)


def get_hashes() -> HashResponse:
    hashes = Hash.query.order_by(Hash.created_at).all()
    names = [Item.query.get(h.item_id).name for h in hashes]
    return HashResponse(list(zip(hashes, names)))


def get_store() -> StoreResponse:
    regular = Item.query.filter_by(limited=False).all()
    limited = Item.query.filter_by(limited=True).all()
    limited_available, limited_unavailable = [], []
    for item in limited:
        if item.item_hashes:
            limited_unavailable.append(item)
        else:
            limited_available.append(item)
    return StoreResponse(regular, limited_available, limited_unavailable)


def check_item(name: str) -> bool:
    return Item.query.filter_by(name=name).first() is not None
