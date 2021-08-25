from flask import Flask, render_template, jsonify
import duolingo
import os
from markupsafe import escape

class Session:
    def __init__(self, username, password):
        self.lingo = duolingo.Duolingo(username, password)

def create_app():
    project_root = os.path.dirname(__file__)
    template_path = os.path.join(project_root, './templates')
    
    '''
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
        
    lingo = Session(username, password)
    '''
    
    app = Flask(__name__, template_folder=template_path)
    app.config['TESTING'] = True
    

    @app.route('/hello')
    def hello_world():
        return render_template('hello.html')
    
    @app.route('/hi/<name>')
    def hi(name):
        return f"<p>Hi {escape(name)}!</p>"
        
    @app.route('/auth')
    def auth():
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')
        lingo = duolingo.Duolingo(username, password)
        return jsonify(lingo.get_known_words('es'))
        '''
        user = os.getenv('USERNAME')
        print (user)
        return user
        '''
    @app.route('/chopstick/')
    def chopstick():
        chopstick = {
            'color': 'bamboo',
            'left_handed': True
        }
        return jsonify(chopstick)
        
    return app

if __name__== "__main__":
    app = create_app()
    app.run()