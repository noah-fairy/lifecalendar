import os

from src.config.local import LocalConfig
from src.config.production import ProductionConfig


def build_config():
    env = os.environ.get("ENV", "local")
    print(f'----- build config with "{env}" environment -----')

    match env:
        case "local":
            return LocalConfig()
        case "production":
            return ProductionConfig()
        case _:
            raise ValueError(f"unknown environment: {env}")


config = build_config()
