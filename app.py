from flask import Flask, render_template, request, jsonify
from session import Session
import duolingo
import os
from markupsafe import escape
from flask_cors import cross_origin
import json

def create_app():
    project_root = os.path.dirname(__file__)
    template_path = os.path.join(project_root, './templates')
    
    app = Flask(__name__, template_folder=template_path)
    app.config['TESTING'] = True
    

    @app.route('/hello')
    def hello_world():
        return render_template('hello.html')
    
    @app.route('/hi/<name>', methods = ['GET', 'POST'])
    @cross_origin()
    def hi(name):
        return f"<p>Hi {escape(name)}!</p>"
        
    @app.route('/auth/<string:lang>', methods = ['GET', 'POST'])
    @cross_origin()
    def auth(lang):
        lang = escape(lang)
        duoPairs = {}
        if (app.config['TESTING'] == True) and (request.method == 'GET'):
            print ("Testing config is on!")
            username = os.getenv('USERNAME')
            password = os.getenv('PASSWORD')
            duoPairs = getDuoPairs(username, password, escape(lang))
        elif request.method == 'POST':
            print ("POST method is true")
            cred = json.loads(request.data.decode("utf-8"))
            duoPairs = getDuoPairs(cred['username'], cred['password'], lang)
        return jsonify(duoPairs)
        
    def getDuoPairs(username, password, lang):
        known_words = []
        known_pairs = {}
        try:
            lingo = duolingo.Duolingo(username, password)
            known_words = lingo.get_known_words(lang)
            known_pairs = lingo.get_translations(known_words, source='es', target='en')
        except KeyError:
            print ("language not learned")
        return known_pairs
        
    return app

if __name__== "__main__":
    app = create_app()
    app.run(port=6500)