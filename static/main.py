from flask import Flask, render_template, request
import pandas as pd
import csv

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/data", methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        f = request.form['csvfile']
        data = []
        with open(f) as file:
            csvfile = csv.reader(file)
            for r in csvfile:
                data.append(r)
        return render_template('data.html')

@app.route("/showdata", methods=['GET', 'POST'])
def showdata():
    if request.method == 'POST':
        f = csv.DictReader(open('static/names.csv'))
        data = []
        for r in f:
            data.append(r)
        return render_template('showdata.html', data=data)

@app.route("/room", methods=['GET', 'POST'])
def room():
    if request.method == 'POST':
        room = request.form['room']
        csv_reader = csv.DictReader(open('static/names.csv'))
        temp_path = ''
        temp_name = ''
        for r in csv_reader:
            if room == r['Room']:
                temp_path = '../static/'+r['Picture']
                temp_name = r['Name']

        if temp_path != '' or temp_name != '':
            return render_template('room.html', image_path=temp_path, name=temp_name, message="found")
        else:
            return render_template('room.html', error="Picture and Name did not find for Room!")

@app.route("/grade", methods=['GET', 'POST'])
def grade():
    if request.method == 'POST':
        g1 = request.form['g1']
        g2 = request.form['g2']
        csv_reader = csv.DictReader(open('static/names.csv'))
        temp_path = ''
        temp_name = ''
        temp_state = ''
        for r in csv_reader:
            if g1 >= r['Grade'] and g2 <= r['Grade']:
                temp_path = '../static/'+r['Picture']
                temp_name = r['Name']
                temp_state = r['State']
                return render_template('grade.html', image_path=temp_path, name=temp_name, state=temp_state,
                                       message="found")

        if temp_path == '' or temp_name == '' or temp_state == '':
            return render_template('grade.html', error="Picture and Name did not find for Room!")

if __name__ == "__main__":
    app.run(debug=True)