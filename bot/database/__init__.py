from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import create_async_engine

from data import Config
from database.models import BaseModel

def get_engine() -> Engine:
    engine: Engine = create_async_engine(
        url=Config.url,
        echo=False,
        future=True
    )

    return engine