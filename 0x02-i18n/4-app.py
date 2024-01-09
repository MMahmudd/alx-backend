#!/usr/bin/env python3
"""A_simple_flask_app
"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """_summaries/

    Returns:
            type: descriptions
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# configure_the_flask_app
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """_summaries/

    Returns:
            type: ddescriptions
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        print(locale)
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])

# babel.init_appl(app,_locale_selector==get_local)


@app.route('/')
def index():
    """_summaries
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
