from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

class Settings:
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")


settings = Settings()

# print("HOST:", settings.DB_HOST)
# print("PORT:", settings.DB_PORT)
# print("USER:", settings.DB_USER)
# print("PASSWORD:", settings.DB_PASSWORD)
# print("DATABASE:", settings.DB_NAME)