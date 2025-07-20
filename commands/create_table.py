import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from config import admin_url, dbname
from sqlalchemy import inspect
from database import engine, get_session
from models import users
from .base import Command

# Команда для инициализации таблицы users
class CreateTableCommand(Command):
    # Создаем таблицы по ORM модели
    def run(self):
        self.ensure_database()
        with get_session() as session:
            inspector = inspect(engine)
            if not inspector.has_table("users"):
                print("Creating tables...")
                users.metadata.create_all(engine)
                print("Tables created successfully.")
            else:
                print("Database and tables already exist.")
                
    # Проверяем, существует ли база данных, если нет, то создаем её
    def ensure_database(self):
        with psycopg2.connect(admin_url) as con:
            con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            with con.cursor() as cur:
                cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (dbname,))
                if not cur.fetchone():
                    cur.execute(f"CREATE DATABASE {dbname}")
                    print(f"Database '{dbname}' created.")
                else:
                    print(f"Database '{dbname}' already exists.")

    

