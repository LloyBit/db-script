from database import get_session
from sqlalchemy import text
from datetime import date

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def run():
    with get_session() as session:
        # Получаем уникальные строки по ФИО+дата рождения
        result = session.execute(text("""
            SELECT DISTINCT full_name, date_of_birth, gender
            FROM users
            ORDER BY full_name
        """))
        rows = result.fetchall()
        for row in rows:
            full_name = row[0]
            dob = row[1]
            gender = row[2]
            age = calculate_age(dob)
            print(f"{full_name:40} {dob.strftime('%Y-%m-%d'):15} {gender:8} {age:12}")