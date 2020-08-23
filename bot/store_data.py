import psycopg2

from gather_data import get_file


def stock_to_db(json_data):
    """
    Function to store stock data in available db

    Parameters
    ----------
    json_data : dictionary with data to be stored.
    """
    settings = get_file('.settings')
    db_connection = psycopg2.connect(host=settings['db_host'],
                                     port=settings['db_port'],
                                     database=settings['db_name'],
                                     user=settings['db_user'],
                                     password=settings['db_passwd'])

    cursor = db_connection.cursor()
    cursor.execute("""SELECT * FROM django_migrations""")
    cursor.execute("""SELECT * FROM django_migrations""")
    result = cursor.fetchall()
    print(result)
