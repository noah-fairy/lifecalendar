import os


class ProductionConfig:
    DATABASE_URL = os.environ.get("DATABASE_URL", "").replace(
        "postgres://", "postgresql://", 1
    )  # heroku uses postgres:// but sqlalchemy uses postgresql:// after 1.4
