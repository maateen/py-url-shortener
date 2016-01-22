from app.utils import short_url_generator
from app.utils import url_checker
from flask import request


def apiv10(long_url):
    # This is our Version-1.0 API function. It will take the long_url as
    # parameter then return two different dictionary based on url_checker
    # function output.
    checker = url_checker(long_url)
    if checker is True:
        short_url = short_url_generator(long_url)
        return {'short_url': short_url}
    else:
        error = "The URL seems to be dead at this moment."
        return {'error': error}
