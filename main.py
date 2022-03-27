import json

import pygal
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin

import dao

app = Flask(__name__)
CORS(app)


@app.route('/', methods={'GET'})
def index():
    bar_chart = pygal.Bar()
    bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
    chart = bar_chart.render_data_uri()

    data = dao.getAudits()
    return render_template('dashboard.html', chart1=chart)


@app.route('/getAudits', methods={'GET'})
@cross_origin()
def getAudits():
    return jsonify(dao.getAudits()), 200\

@app.route('/getSettings', methods={'GET'})
@cross_origin()
def getSettings():
    return jsonify(dao.getSettings()), 200


@app.route('/settings', methods={'GET'})
def settings():
    return render_template('settings.html', attr="test val")


@app.route('/collector', methods={'POST'})
def collector():
    data = request.get_json(silent=True)
    for audit in data:
        dao.createAudit(audit)
    response = {
        'data': data
    }
    return response, 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
