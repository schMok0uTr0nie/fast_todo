import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from todo.config import Settings

BASE_DIR = os.path.dirname(os.path.abspath(__name__))

db_path = os.path.join(BASE_DIR, 'todo', 'database', 'DB')
if not os.path.exists(db_path):
    os.makedirs(db_path)

Base = declarative_base()

engine = create_engine(Settings.db_url, connect_args={'check_name_thread': False}, echo=True)


def get_db():
    db_session_local = SessionLocal()
    try:
        yield db_session_local
    finally:
        db_session_local.close()


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
