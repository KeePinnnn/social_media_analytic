from flask import Flask, send_from_directory, request, Response, render_template, jsonify

from test import demo

import subprocess
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return "hello world"

@app.route('/detector')
def detector():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/get_details', methods=['GET'])
def get_info():
    username = request.args['username']
    content = request.args['content']
    if os.path.exists('./result.txt'):
        os.remove('./result.txt')
    if username and content:
        subprocess.Popen(['python', 'test.py', username, content]).pid
    
    while True:
        if os.path.exists('./result.txt'):
            with open('./result.txt', 'r') as file:
                data = file.read()
                if data:
                    return jsonify(result=data), 200
        else:
            continue
        
@app.route('/<path:path>', methods=['GET'])
def get_fonts(path):
    return app.send_static_file(path)

if __name__ == "__main__":
    app.run(debug=True)