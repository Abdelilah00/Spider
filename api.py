import json

import pygal
from flask import Flask, render_template, request, jsonify

import dao

app = Flask(__name__)


@app.route('/', methods={'GET'})
def index():
    data = dao.getAudits()
    print(data)
    graph = pygal.Line()
    graph.title = '% Change Coolness of programming languages over time.'
    graph.x_labels = ['2011', '2012', '2013', '2014', '2015', '2016']
    graph.add('Python', [15, 31, 89, 200, 356, 900])
    graph.add('All others combined!', [5, 15, 21, 55, 92, 105])
    graph_data = graph.render_data_uri()

    return render_template('dashboard.html', chart=graph_data)


@app.route('/getAudits', methods={'GET'})
def getAudits():
    return jsonify(dao.getAudits()), 200


@app.route('/getSettings', methods={'GET'})
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
