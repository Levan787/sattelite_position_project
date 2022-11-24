import psycopg2

from configs.constants import SATELLITE_LATITUDE, SATELLITE_LONGITUDE, NEAREST_COUNTRY_NAME
from configs.db_config import *


class PsqlDriver:
    def __init__(self, host=HOSTNAME,
                 database=DATABASE,
                 user=USERNAME,
                 password=PASSWORD,
                 port=PORT_ID):
        self.driver = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        self.cur = self.driver.cursor()

    def execute(self, query):
        """execute and commit raw and table queries"""
        if "SELECT" in query.lower():
            return self.cur.fetchall()
        self.cur.execute(query)
        self.driver.commit()

    def create_table(self, table_name: str):
        """if table does not exist create table and insert rows"""
        query = f"""CREATE TABLE IF NOT EXISTS {table_name}(
                              {SATELLITE_LONGITUDE} float,
                              {SATELLITE_LATITUDE}  float,
                             {NEAREST_COUNTRY_NAME} varchar
                          ); """
        self.execute(query)
        return query

    def insert_row(self, table_name: str, column_names: list, dictionary_values: dict):
        """insert satellite coordinates and country name values in postgres table"""
        query = f"""insert into {table_name}({', '.join(column_names)})
                            VALUES ({', '.join(dictionary_values.values())});
                            """
        self.execute(query)
        return query
