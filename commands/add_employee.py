from database import get_session
from models import users
from .base import Command

class AddEmployeeCommand(Command):
    # Добавляем сотрудника в таблицу users
    def run(self, args):
        with get_session() as session:
            session.add(users(full_name=args[0], date_of_birth=args[1], gender=args[2]))