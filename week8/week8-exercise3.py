#!flask/bin/python
from flask import Flask, jsonify, abort, request
import pandas as pd
import pymysql

app = Flask(__name__)

cnx = pymysql.connect(user='dev', password='ax2',
                      host='127.0.0.1', port=3307, db='python')


@app.route('/corona/api/all', methods=['GET'])
def get_all():
    df = pd.read_sql('SELECT * FROM CORVID19', con=cnx)
    all = df.to_dict('records')
    return jsonify({'all': all})


@app.route('/corona/api/<string:country>', methods=['GET'])
def get_numbers(country):

    query = 'SELECT * FROM CORVID19 WHERE Country = "{country}"'.format(
        country=country)
    df = pd.read_sql(query, con=cnx)
    result = df.to_dict('records')

    if len(result) == 0:
        abort(404)
    return jsonify({'country': result[0]})


if __name__ == '__main__':
    app.run(debug=True)
