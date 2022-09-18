class Config:
    TESTING = False


class DevelopmentConfig(Config):
    TESTING = False


class ProductionConfig(Config):
    TESTING = False
