import os 

from flask import Flask

def create_app():
    print('Starting TODO App')
    app = Flask(__name__)

    file_path = os.path.abspath(os.getcwd())+"\_todo.db"
    print(file_path)

    app.config.from_mapping(
        FLASK_DEBUG=True,
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///'+file_path    
    )
   
    @app.route('/hello')
    def hello():
        return "Hello, World"

    from todo_app import db
    
    db = db.config_db(app)
    
    from todo_app import views
    app.register_blueprint(views.view)

    return app
