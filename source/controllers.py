from config import logger
from models import Item, Order, db
from schemas import OrderRequest, OrderResponse


def add_order(req: OrderRequest) -> OrderResponse:
    try:
        item = Item.query.filter_by(size=req.size).first()
        if not item:
            raise ValueError("Shirt Size Missing")
        if item.inventory <= 0:
            raise ValueError(f"{item.size} Is Out Of Inventory")
        order = Order(
            first=req.first,
            last=req.last,
            email=req.email,
            phone=req.phone,
            item_id=item.id,
        )
        db.session.add(order)
        db.session.add(item)
        db.session.commit()
    except ValueError as e:
        logger.info(e)
        return OrderResponse(succeeded=False)
    return OrderResponse(succeeded=True)
