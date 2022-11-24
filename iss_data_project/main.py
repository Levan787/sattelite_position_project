from dags.psql_connector.PSQLDriver import PsqlDriver
from dags.open_csv import write_to_csv
from dags.configs.constants import CSV_FILE
from dags.json_data import merge_dictionary
from dags.configs.constants import SATELLITE_LATITUDE, SATELLITE_LONGITUDE, \
    NEAREST_COUNTRY_NAME, TABLE_NAME


def main():
    column_names = [SATELLITE_LONGITUDE, SATELLITE_LATITUDE, NEAREST_COUNTRY_NAME]
    satellite_data = merge_dictionary()
    sql = PsqlDriver()

    sql.execute(sql.create_table(TABLE_NAME))
    sql.execute(sql.insert_row(TABLE_NAME, column_names, satellite_data))
    write_to_csv(CSV_FILE, satellite_data)


if __name__ == '__main__':
    main()
