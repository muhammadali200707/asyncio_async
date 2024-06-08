import os
import psycopg2 as psql
from dotenv import load_dotenv

load_dotenv()


class Database:
    @staticmethod
    def connect(query: str, query_type: str) -> str or list:
        """

        :param query: "SELECT * FROM address "
        :param query_type: select, insert, delete, update
        :return:str or list
        """

        db = psql.connect(
            database=os.getenv("database"),
            user=os.getenv("user"),
            password=os.getenv("password"),
            host=os.getenv("localhost"),
            port=os.getenv("5432")
        )
        cursor = db.cursor()
        cursor.execute(query)
        print(cursor.fetchall())
