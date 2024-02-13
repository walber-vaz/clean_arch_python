import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "mysql+pymysql://{}:{}@{}:{}/{}".format(
            DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
        )
        self.__engine = self.__create_database_engine()

    def __create_database_engine(self):
        return create_engine(self.__connection_string)

    def get_engine(self):
        return self.__engine
