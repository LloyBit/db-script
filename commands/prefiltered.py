from database import get_session
from sqlalchemy import text
from .base import Command
from utils import timer

# Команда для выполнения запроса с фильтрацией
class PrefilteredCommand(Command):
    @timer
    def run(self):
        with get_session() as session:
            result = session.execute(text("""
                SELECT full_name, date_of_birth, gender
                FROM users
                WHERE gender = 'MALE' AND full_name LIKE 'F%'
                ORDER BY full_name
            """))
            rows = result.fetchall()
            for row in rows:
                full_name = row[0]
                dob = row[1]
                gender = row[2]
                print(f"{full_name:40} {dob.strftime('%Y-%m-%d'):15} {gender:8}")
