from flask import Flask

from config import config

#Routes
from routes import moves

app=Flask(__name__)


def page_not_foun(error):
    return "<h1>Not found page papu!!</h1>",404

if __name__=='__main__':
    app.config.from_object(config['development'])
    
    
    #Blueprints
    app.register_blueprint(moves.main,url_prefix='/api/movies')
    
    #Error handlers
    app.register_error_handler(404,page_not_foun)
    app.run()