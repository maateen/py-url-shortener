from flask_wtf import Form
from wtforms.fields.html5 import URLField
from wtforms.validators import url


class GetLinkForm(Form):

    # We are making a form instantiating Form class from flask_wtf, mainly for
    # getting URL as input from users and also for validating URL.
    long_url = URLField(validators=[url()])
