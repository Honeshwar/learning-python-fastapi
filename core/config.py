import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class BaseSettings:
    PROJECT_NAME: str = "Nation First"
    PROJECT_VERSION: str = "1.0.0"
    ENV = os.getenv("ENV")


    S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
    AWS_SECRET_ACCESS_KEY = os.getenv("aws_secret_access_key")
    AWS_ACCESS_KEY_ID = os.getenv("aws_access_key_id")


class Settings(BaseSettings):
    MYSQL_USER: str = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_SERVER: str = os.getenv("MYSQL_SERVER", "localhost")
    # default mysql port is 3306
    MYSQL_PORT: str = os.getenv("MYSQL_PORT", 3306)
    MYSQL_DB: str = os.getenv("MYSQL_DB", "tdd")

    MYSQL_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DB}"


class TestSettings(BaseSettings):
    MYSQL_USER: str = os.getenv("MYSQL_TEST_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_TEST_PASSWORD")
    MYSQL_SERVER: str = os.getenv("MYSQL_TEST_SERVER", "localhost")
    # default mysql port is 3306
    MYSQL_PORT: str = os.getenv("MYSQL_TEST_PORT", 3306)
    MYSQL_DB: str = os.getenv("MYSQL_TEST_DB", "tdd")
    MYSQL_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DB}"


settings = Settings()
test_settings = TestSettings()
base_settings = BaseSettings()
