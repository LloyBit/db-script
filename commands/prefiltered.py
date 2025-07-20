from database import get_session
from sqlalchemy import text
from .base import Command
from utils import timer

class PrefilteredCommand(Command):
    @timer
    def run(self):
        with get_session() as session:
            result = session.execute(text("""
                SELECT COUNT(*) 
                FROM users 
                WHERE gender = 'MALE' AND full_name LIKE 'F%'
            """))
            count = result.scalar()
            print(f"Найдено записей: {count}")

