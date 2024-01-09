#!/usr/bin/env python3
"""A_simple_flask_app
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """_summaries/

    Returns:
                    type: descriptions/
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# configure_the_flask_app
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """returns_a_user_dictionary_or_None_if_the_ID_cannot_be_found
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """_summaries/
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """_summaries/

    Returns:
                    type: descriptions
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        print(locale)
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])

# babe_l.init_app_app,_locale_selector==get_local)


@app.route('/')
def index():
    """summaries/
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
