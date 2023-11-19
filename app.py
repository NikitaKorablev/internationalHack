from flask import Flask, jsonify, render_template

import configparser
config = configparser.ConfigParser()
config.read('./config.ini')

app = Flask(__name__)

json_template = {
    'status': True,
    'data': ''
}
 
@app.route('/api/v1.0/check', methods=['GET'])
def check():
    return jsonify(json_template)

@app.route('/api/v1.0/get', methods=['GET'])
def get():
    answer = json_template.copy()

    # операции с answer
    
    return jsonify(answer)

@app.route('/api/v1.0/post', methods=['POST'])
def post():
    answer = json_template.copy()

    # операции с answer
    
    return jsonify(answer)

@app.route('/')
def main():

    # вывод главной страницы

    return render_template('main.html')

if __name__ == '__main__':
    app.run()