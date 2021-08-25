from flask import Flask, render_template, jsonify
import duolingo
import os
from markupsafe import escape

def create_app():
    project_root = os.path.dirname(__file__)
    template_path = os.path.join(project_root, './templates')
    
    app = Flask(__name__, template_folder=template_path)
    app.config['TESTING'] = True

    @app.route('/hello')
    def hello_world():
        return render_template('hello.html')
    
    @app.route('/hi/<name>')
    def hi(name):
        return f"<p>Hi {escape(name)}!</p>"
        
    @app.route('/user')
    def user():
        pass
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
        #print (jsonify(chopstick).json)
        #print (jsonify(chopstick['color']).json)
        return jsonify(chopstick)
        
    return app

if __name__== "__main__":
    app = create_app()
    app.run()