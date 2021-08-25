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
    
    app = Flask(__name__, template_folder=template_path)
    app.config['TESTING'] = True
    

    @app.route('/hello')
    def hello_world():
        return render_template('hello.html')
    
    @app.route('/hi/<name>')
    def hi(name):
        return f"<p>Hi {escape(name)}!</p>"
        
    @app.route('/auth/<string:lang>')
    def auth(lang):
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')
        known_words = []
        known_pairs = {}
        try:
            lingo = duolingo.Duolingo(username, password)
            known_words = lingo.get_known_words(lang)
            known_pairs = lingo.get_translations(known_words, source='es', target='en')
        except KeyError:
            print ("language not learned")
        return jsonify(known_pairs)
        
    return app

if __name__== "__main__":
    app = create_app()
    app.run()