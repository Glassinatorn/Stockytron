import pandas as pd
import psycopg2

from gather_data import get_file


def stock_to_db(json_data, stock_name, db_name):
    """
    Function to store stock data in available db

    Parameters
    ----------
    json_data : dictionary with data to be stored.
    """
    table = json_data[5]
    print(stock_name)
    # storing the data as csv file
    df = pd.read_json(json_data)
    df.set_index('date', inplace=True)
    df.to_csv(stock_name + '.csv')

    # setting up connection to db
    settings = get_file('.settings')
    db_connection = psycopg2.connect(host=settings['db_host'],
                                     port=settings['db_port'],
                                     database=settings[db_name],
                                     user=settings['db_user'],
                                     password=settings['db_passwd'])
    cursor = db_connection.cursor()

    f = open(stock_name + '.csv')
    cursor.copy_from(f, '"' + stock_name.lower() + '"')

    # importing data from created csv file into db
    #cursor.execute("COPY " + " FROM " + " CSV")
    #result = cursor.fetchall()
    #print(result)
