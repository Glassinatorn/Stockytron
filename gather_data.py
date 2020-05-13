"""Gather data and credentials

This file simply contains functions meant to gather data and credentials.

"""

import json
import requests

def get_tokens(token_file):
    """
    Function to gather tokens from a file containing them.

    The function gathers data from the file ".token".

    Parameters
    ----------
    token_file : string
        The name of the file to get tokens from.

    Returns
    -------
    Dictionary
        Contains the tokens from the specified file.
    """

    with open(token_file, 'r') as tmp_file:
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
