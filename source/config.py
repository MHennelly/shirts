import logging.config
import os
import secrets

from dotenv import load_dotenv


class Config:
    SECRET_KEY = secrets.token_urlsafe(32)

    def __init__(self):
        load_dotenv()
        self.TESTING = os.environ.get("TESTING", False)
        self.MIGRATING = os.environ.get("MIGRATING", False)
        self.ENV = os.environ["ENV"]
        self.ALPHA = os.environ["ALPHA"]
        self.SQLALCHEMY_DATABASE_URI = (
            os.environ["SQLALCHEMY_DATABASE_URI_PROD"]
            if self.ENV == "PROD"
            else os.environ["SQLALCHEMY_DATABASE_URI_DEV"]
        )


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("shirts.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)
