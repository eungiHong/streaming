from flask import Flask
from flask_migrate import Migrate

def create_app():

    app = Flask(__name__)
    
    # Blueprint
    from .views import main_views, stream_views
    app.register_blueprint(main_views.bp)    
    app.register_blueprint(stream_views.bp)

    return app
