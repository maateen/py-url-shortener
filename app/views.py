from app import app
from app.api import apiv10
from app.form import GetLinkForm
from app.models import Urls
from app.utils import number_of_generated_short_url
from app.utils import short_url_generator
from app.utils import url_checker
from flask import abort
from flask import flash
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for


@app.route('/', methods=['GET', 'POST'])
def home():
    # This function is executed when http://example.com/ is requested. It
    # works with two methods - GET and POST. When URL is submitted via POST
    # method, then it catches it and show the regarding short URL or regarding
    # errors.

    number = number_of_generated_short_url()
    if request.method == 'POST':
        form = GetLinkForm(request.form)
        if form.validate():
            long_url = form.long_url.data
            checker = url_checker(long_url)
            if checker is True:
                short_url = short_url_generator(long_url)
                return render_template('index.html', form=form,
                                       short_url=short_url, number=number)
            else:
                flash("The URL seems to be dead at this moment.")
                return render_template('index.html', form=form, number=number)
        else:
            flash("Please, paste a valid link to shorten it.")
            return render_template('index.html', form=form, number=number)

    else:
        return render_template('index.html', form=GetLinkForm(), number=number)


@app.route('/<string:short_url>')
def redirect_to_main_url(short_url):
    # When a short URL comes to this app, the short URL will be redirected to
    # the long URL, we mean main URL. This function does this important task.
    # If the short URL isn't in our database, then it throws 404 error
    # message.

    surl_query = Urls.query.filter_by(short_url=short_url).first()
    if surl_query is None:
        abort(404)
    else:
        return redirect(surl_query.long_url)


@app.route('/api/<string:version>/', methods=['POST'])
def api(version):
    # This function handles our API requests. Firstly it checks the api
    # version, if not matches, then it throws a 403 error message. If matched,
    # then it triggers the equivalent api function.

    if version == 'v1.0' and not request.json:
        long_url = request.get_json().get('long_url')
        info = apiv10(long_url)
        return jsonify(info)
    else:
        abort(403)


@app.errorhandler(404)
def page_not_found(error):
    # This function handles all 404 error on the app and shows a custom 404
    # error page.

    number = number_of_generated_short_url()
    return render_template('404.html', number=number), 404
