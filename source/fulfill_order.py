import sys

from app import app
from config import logger
from models import Item, Order, db


def main(argv: list[str]) -> None:
    with app.app_context():
        try:
            if len(argv) != 2:
                raise ValueError(
                    "First Arg Needs To Be Order ID, 2nd Needs To Be Its Hash"
                )
            order = Order.query.get(argv[0])
            order.fulfilled = True
            order.hash = argv[1]
            item = Item.query.get(order.item_id)
            item.inventory -= 1
            db.session.add(order)
            db.session.add(item)
            db.session.commit()
        except ValueError as e:
            logger.error(e)


if __name__ == "__main__":
    main(sys.argv[1:])
