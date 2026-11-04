from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    if not SECRET_KEY:
        raise ValueError("SECRET_KEY is missing from .env")

    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("DATABASE_URL is missing from .env")