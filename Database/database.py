from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import config


DATABASE_URL = "postgresql+asyncpg://{}:{}@{}/{}".format(
    config.database_user.get_secret_value(),
    config.database_password.get_secret_value(),
    config.database_host.get_secret_value(),
    config.database_name.get_secret_value()
)

async_engine = create_async_engine(DATABASE_URL, echo=False)
async_session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    autoflush=False
)
