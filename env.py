from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context
from database import Base
import os

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://neondb_owner:npg_9CZg6seJHuiY@ep-steep-wind-a4rzln6i-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require")

def run_migrations_offline():
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    engine = create_engine(DATABASE_URL, poolclass=pool.NullPool)
    with engine.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()