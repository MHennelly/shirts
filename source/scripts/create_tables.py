from source.app import app
from source.config import logger
from source.models import db


def main() -> None:
    with app.app_context():
        logger.info("Running db.create_all")
        db.create_all(app=app)
        logger.info("DB Initialized")


if __name__ == "__main__":
    main()
