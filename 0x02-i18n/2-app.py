#!/usr/bin/env python3
"""A_simple_flask_app
"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """summaries/

    Returns:
            type: ddescriptions/
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# configure_the_flask_app
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """summaries/

    Returns:
            type: descriptions/
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """_summ_ary_
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
