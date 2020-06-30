"""Gathers data and credentials

This file simply contains functions meant to gather data and credentials.
"""

import json
import requests
import pandas as pd

def get_file(data_file):
    """
    Function to gather data from a json or csv file.

    Parameters
    ----------
    file : String
        The name of the file to get data from.

    Returns
    -------
    Dictionary
        Contains the data from the specified file.
    """

    if "csv" in data_file:
        data = pd.read_csv(data_file).to_json()

    else:
        with open(data_file, 'r') as tmp_file:
            data = json.loads(tmp_file.read())

    return data


def get_data(URL):
    """
    Gathers data from given URL source.

    The function makes a https request to the given URL source. The function
    does not add any parameters to the URL so the URL should be complete before
    sending it in to the function.

    Parameters
    ----------
    URL : String
        The URL string that data is to be gathered from.

    Returns
    -------
    Dictionary
        Contains the gathered data.
    """

    ses = requests.session()
    ses.verify = '/etc/ssl/certs/ca-certificates.crt'
    response = requests.get(URL)

    return json.loads(response.content)


def get_all(tokens, sources):
    """
    Function to get all the latest data

    Parameters
    ----------
    tokens : Dictionary
        Contains all the tokens for various sources.
    sources : Dictionary
        Contains all the sources to gather data from.

    Returns
    -------
    Dictionary
        Contains the gathered data.
    """

    all_data = {}

    for source in sources:
        total_url = sources[source]["demo"] + tokens[source]["demo"]
        tmp = get_data(total_url)
        all_data.update({source: tmp})

    return all_data


def recr_dict_search(obj, search, result):
    """
    Searches a dictionary recursively until the sought after field is found.

    Parameters
    ----------
    obj : Dictionary
        The dictionary which is to be searched through.
    search : String
        The sought after field.
    result : Array
        The array which values from the sought after field is to be appended
        into.

    Returns
    -------
    Array
        Contains the searched data.
    """

    for key in obj:
        if search in obj[key]:
            result.extend([obj[key][search]])
        elif type(obj[key]) == dict:
            recr_dict_search(obj[key], search, result)

