'''
Initializes and configures the backend Flask application for aeryck.com

Methods
-------
create_app(test_config=None)
    create the application

[1] https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/
'''
import os

from flask import Flask

def create_app(test_config=None):
    '''
    Parameters
    ----------
    test_config : file, optional
        a file path to a configuration file

    Attributes
    ----------
    app : Flask
        instnace of Flask to be configured for aeryck.com
            __name__ is the name of the current python module, aeryck

            instance_relative_config=True indicated that configuration files
            are relative to the instance folder. The instance folder is
            designed to not be under version control, such as the secret key,
            the database file, etc. [1]
    Returns
    -------
    app : Flask
        instance of Flask configured for aeryck.com

    '''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
