from config import db_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager


engine = create_engine(db_url, echo=False)
SessionLocal = sessionmaker(bind=engine)

# Контекстный менеджер для работы с сессией и ее авто-закрытия 
@contextmanager
def get_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
