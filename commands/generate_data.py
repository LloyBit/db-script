from faker import Faker
from utils import timer
from database import get_session
from psycopg2.extras import execute_values
import numpy as np
from .base import Command

fake = Faker()

class GenerateDataCommand(Command):
    @timer
    def run(self):
        self.generate_fake_users()

    def recreate_indexes(self, cursor):
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_users_fullname ON users(full_name);")

    def generate_fake_users(self):
        # Управление пакетной вставкой
        num_packages = 1000
        users_per_package = 1000
        
        # Уменьшение значений увеличит количество не уникальных значений но увеличит производительность
        # Для тестирования 3-го задания
        first_names_pool = 1000
        last_names_pool = 1000
        middle_names_pool = 1000
        date_pool = 1000

        with get_session() as session:
            conn = session.connection().connection
            cursor = conn.cursor()

            # Отключаем индексы перед массовой вставкой
            cursor.execute("DROP INDEX IF EXISTS idx_users_fullname;")
            conn.commit()

            # Готовый пул данных для комбинирования
            date_pool_arr = np.array([fake.date_of_birth(minimum_age=18, maximum_age=80) for _ in range(date_pool)])
            last_names = np.array([fake.last_name() for _ in range(last_names_pool)])
            first_names = np.array([fake.first_name() for _ in range(first_names_pool)])
            middle_names = np.array([fake.first_name() for _ in range(middle_names_pool)])

            # Вставка 100 мужчин с фамилией на F
            bulk_test_users = []
            for _ in range(100):
                ln = fake.last_name()
                ln = "F" + ln[1:]
                fn = np.random.choice(first_names)
                mn = np.random.choice(middle_names)
                dob = np.random.choice(date_pool_arr)
                g = "MALE"
                bulk_test_users.append((f"{ln} {fn} {mn}", dob, g))
            insert_query = "INSERT INTO users (full_name, date_of_birth, gender) VALUES %s"
            execute_values(cursor, insert_query, bulk_test_users)
            conn.commit()

            # Пакетная вставка 
            for _ in range(num_packages):
                # Вектора с данными 
                genders = np.random.choice(['MALE', 'FEMALE'], size=users_per_package)
                last_names_selected = np.random.choice(last_names, size=users_per_package)
                first_names_selected = np.random.choice(first_names, size=users_per_package)
                middle_names_selected = np.random.choice(middle_names, size=users_per_package)
                dates_selected = np.random.choice(date_pool_arr, size=users_per_package)
                
                # Объединение векторов в строку запроса
                users_data = [
                    (f"{ln} {fn} {mn}", dob, g)
                    for ln, fn, mn, dob, g in zip(last_names_selected, middle_names_selected, first_names_selected, dates_selected, genders)
                ]
                insert_query = "INSERT INTO users (full_name, date_of_birth, gender) VALUES %s"
                execute_values(cursor, insert_query, users_data)
                conn.commit()

            # Восстанавливаем индексы после вставки
            cursor.execute("CREATE INDEX idx_users_fullname ON users(full_name);")
            conn.commit()
