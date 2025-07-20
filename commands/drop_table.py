from database import get_session
from sqlalchemy import text
from .base import Command

# Команда для удаления таблицы users
class DropTableCommand(Command):
    def run(self):
        with get_session() as session:
            session.execute(text("DROP TABLE IF EXISTS users"))