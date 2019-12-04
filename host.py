from flask import Flask, send_from_directory, request

from test import demo

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
    if username and content:
        print(demo(username, content))

    return 0

if __name__ == "__main__":
    app.run(debug=True)