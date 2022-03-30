import json

import pygal
from flask import Flask, render_template, request, jsonify
import pandas as pd
from pandas import unique

import dao

app = Flask(__name__)


@app.route('/', methods={'GET'})
def index():
    data = dao.getAudits()
    print(data)
    table = pd.json_normalize(data)
    users = table.user.unique()

    graph = pygal.Line()
    graph.title = '% Cpu Consumption'
    graph.x_labels = table['createdon'].values
    for user in users:
        graph.add(user, table[table.user == user].cpu)
    graph1 = graph.render_data_uri()

    graph = pygal.Line()
    graph.title = '% Storage Consumption'
    graph.x_labels = table['createdon'].values
    for user in users:
        graph.add(user, table[table.user == user].cpu)
    graph2 = graph.render_data_uri()

    graph = pygal.Line()
    graph.title = '% Memory Consumption'
    graph.x_labels = table['createdon'].values
    for user in users:
        graph.add(user, table[table.user == user].cpu)
    graph3 = graph.render_data_uri()

    return render_template('dashboard.html', graph1=graph1, graph2=graph2, graph3=graph3)


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
