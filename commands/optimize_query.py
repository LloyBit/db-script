from database import get_session
from .base import Command
from utils import timer

class OptimizeQueryCommand(Command):
    @timer
    def run(self):
        with get_session() as session:
            conn = session.connection().connection
            cursor = conn.cursor()
            # Создадим составной индекс
            cursor.execute("""
                CREATE INDEX idx_users_gender_fullname
                ON users(gender, full_name);
            """)
            conn.commit()
            print("Составной индекс (gender, full_name) создан.")

