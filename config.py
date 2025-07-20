from dotenv import load_dotenv
import os

load_dotenv()

dbname = os.getenv("POSTGRES_DB")
if dbname is None:
    raise ValueError("Missing POSTGRES_DB environment variable.")

admin_url = os.getenv("ADMIN_URL")
if admin_url is None:
    raise ValueError("Missing ADMIN_URL environment variable.")

db_url = str(os.getenv("DATABASE_URL"))
if db_url is None:
    raise ValueError("Missing DATABASE_URL environment variable.")