from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename
import os

# папка для сохранения загруженных файлов
UPLOAD_FOLDER = './data_sience/'

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

@app.route('/api/v1.0/post', methods=['POST']) # пока написал здесь созранение файлов
def post():
    answer = json_template.copy()

    print(request.files)
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    # операции с answer
    answer['data'] = filename
    answer['status'] = True
    return jsonify(answer)

@app.route('/')
def main():

    # вывод главной страницы

    return render_template('main.html')

if __name__ == '__main__':
    app.run()