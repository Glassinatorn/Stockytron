from bot.gather_data import get_file


def stock_to_db(json_data):
    """
    Function to store stock data in available db

    Parameters
    ----------
    json_data : dictionary with data to be stored.
    """
    config = get_file('.settings')
