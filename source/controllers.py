from models import Item, Order, db
from schemas import OrderRequest, OrderResponse


def add_order(req: OrderRequest) -> OrderResponse:
    try:
        item = Item.query.filter_by(size=req.size).first()
        assert item
        assert item.inventory > 0
        order = Order(
            first=req.first,
            last=req.last,
            email=req.email,
            phone=req.phone,
            item_id=item.id,
        )
        item.inventory -= 1
        db.session.add(order)
        db.session.add(item)
        db.session.commit()
    except AssertionError:
        return OrderResponse(succeeded=False)
    return OrderResponse(succeeded=True)
