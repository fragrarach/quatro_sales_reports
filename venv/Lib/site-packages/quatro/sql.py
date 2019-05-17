import psycopg2.extensions
from . import files

# PostgreSQL DB connection configs
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)


# Initialize production DB connection, listen cursor and query cursor
def sigm_connect(channel=None):
    if files.dev_check():
        host = '192.168.0.57'
        dbname = 'DEV'
    else:
        host = '192.168.0.250'
        dbname = 'QuatroAir'
    sigm_connection = psycopg2.connect(f"host='{host}' dbname='{dbname}' user='SIGM' port='5493'")
    sigm_connection.set_client_encoding("latin1")
    sigm_connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    if channel:
        sigm_listen = sigm_connection.cursor()
        sigm_listen.execute(f"LISTEN {channel};")
        print(f'Listen channel {channel} open on DB {dbname} at host {host}')
    sigm_db_cursor = sigm_connection.cursor()
    print(f'SIGM cursor open on DB {dbname} at host {host}')

    return sigm_connection, sigm_db_cursor


# Initialize log DB connection, listen cursor and query cursor
def log_connect():
    if files.dev_check():
        host = '192.168.0.57'
    else:
        host = '192.168.0.250'
    log_connection = psycopg2.connect(f"host='{host}' dbname='LOG' user='SIGM' port='5493'")
    log_connection.set_client_encoding("latin1")
    log_connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    log_db_cursor = log_connection.cursor()
    print(f'Log cursor open on DB LOG at host {host}')

    return log_connection, log_db_cursor


# Convert tabular query result to list (2D array)
def tabular_data(result_set):
    lines = []
    for row in result_set:
        line = []
        for cell in row:
            if type(cell) == str:
                cell = cell.strip()
            line.append(cell)
        lines.append(line)
    return lines


# Convert scalar query result to singleton variable of any data type
def scalar_data(result_set):
    for row in result_set:
        for cell in row:
            if type(cell) == str:
                cell = cell.strip()
            return cell


# Query SIGM database
def sql_query(sql_exp, cursor):
    cursor.execute(sql_exp)
    result_set = cursor.fetchall()
    return result_set


if __name__ == "__main__":
    sigm_connect()
    log_connect()
