"""Gathers data and credentials

This file simply contains functions meant to gather data and credentials.
"""

import json
import requests

def get_json_file(json_file):
    """
    Function to gather data from a json file.

    Parameters
    ----------
    json_file : string
        The name of the file to get data from.

    Returns
    -------
    Dictionary
        Contains the data from the specified file.
    """

    with open(json_file, 'r') as tmp_file:
        data = tmp_file.read()

    return json.loads(data)


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
    tokens : dictionary
        Contains all the tokens for various sources.
    sources : dictionary
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
    obj : dict
        The dictionary which is to be searched through.
    search : string
        The sought after field.
    result : array
        The array which values from the sought after field is to be appended
        into.

    Returns
    -------
    array
    """

    for key in obj:
        if search in obj[key]:
            result.extend([obj[key][search]])
        elif type(obj[key]) == dict:
            recr_dict_search(obj[key], search, result)

