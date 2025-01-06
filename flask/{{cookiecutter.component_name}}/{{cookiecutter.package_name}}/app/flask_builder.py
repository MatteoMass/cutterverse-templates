from flask import Flask

from {{cookiecutter.package_name}}.app.controllers.health_controller import bp_health

API_PREFIX = "{{cookiecutter.api_prefix}}"


# Build flask app
# This is in a separate file, so that it can be used with different application servers (Gunicorn, Waitress...)
def create_app():

    application = Flask(__name__)

    application.register_blueprint(bp_health)

    # Register here your blueprints
    # application.register_blueprint(bp_example, url_prefix=API_PREFIX)

    return application


# This must be used as main ONLY LOCALLY!
# Without gunicorn (or another application server),
# the default werkzeug application server is used,
# and thus just a request can be served at a time.
if __name__ == '__main__':

    flask = create_app()
    flask.run(port=8080)