from crypt import methods
from flask import Flask
from flask_restful import Resource, Api
from requests import request
from db_action import get_all_data, save_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)


@app.route('/data')
def get_data():
    response = get_all_data()
    return({'data': response})

@app.route('/save', methods=['POST'])
def put_data():
    resp = save_data(request.json) 
    return({'data': '0k'})    

    

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
