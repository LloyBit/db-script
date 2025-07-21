import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from config import admin_url, dbname
from sqlalchemy import inspect
from database import engine, get_session
from models import Users
from .base import Command

# Команда для инициализации таблицы users
class CreateTableCommand(Command):
    def run(self):
        self.ensure_database()
        self.create_tables_if_not_exists()

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

    def create_tables_if_not_exists(self):
        with get_session() as session:
            inspector = inspect(engine)
            if not inspector.has_table("users"):
                print("Creating tables...")
                Users.metadata.create_all(engine)
                print("Tables created successfully.")
            else:
                print("Database and tables already exist.")


    

