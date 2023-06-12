from flask import Flask, render_template, request
import pandas as pd
import csv
import tempfile
import shutil

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

@app.route("/teln", methods=['GET', 'POST'])
def teln():
    if request.method == 'POST':
        teln = request.form['teln']
        csv_reader = csv.DictReader(open('static/q0c.csv'))
        matching_records = []
        for r in csv_reader:
            if teln == r['teln']:
                matching_records.append({
                    'image_path': '../static/' + r['pic'],
                    'name': r['name'],
                    'description': r['descript']
                })

        if matching_records:
            return render_template('teln.html', records=matching_records, message="found")
        else:
            return render_template('teln.html', error="Picture and Name did not find for Room!")


@app.route("/rnrange", methods=['GET', 'POST'])
def roomnorange():
    if request.method == 'POST':
        rn1 = request.form['rn1']
        rn2 = request.form['rn2']
        csv_reader = csv.DictReader(open('static/q0c.csv'))
        matching_records = []
        for r in csv_reader:
            if rn1 >= r['room'] or rn2 <= r['room']:
                matching_records.append({
                    'image_path': '../static/' + r['pic'],
                    'name': r['name'],
                    'description': r['descript']
                })

        if matching_records:
            return render_template('rnrange.html', records=matching_records, message="found")
        else:
            return render_template('rnrange.html', error="Picture and Name did not find for the given Room no!")


# @app.route("/room", methods=['GET', 'POST'])
# def update_desc():
#     if request.method == 'POST':
#         nm = request.form['name']
#         upddesc = request.form['updated_desc']
#         csv_reader = csv.DictReader(open('static/q0c.csv'))
#         temp_name = ''
#         temp_descript1 = ''
#         for r in csv_reader:
#             if nm == r['name']:
#                 temp_name = r['name']
#                 r['descript'] = upddesc
#                 temp_descript1 = r['descript']
#                 return render_template('room.html', name=temp_name, description=temp_descript1,
#                                        message="found")

#         if temp_name == '' or temp_descript1 == '':
#             return render_template('room.html', error="Picture and Name did not find for Room!")


@app.route("/room", methods=['GET', 'POST'])
def update_desc():
    if request.method == 'POST':
        nm = request.form['name']
        upddesc = request.form['updated_desc']
        csv_file = 'static/q0c.csv'
        temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)

        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            fieldnames = csv_reader.fieldnames
            writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
            for r in csv_reader:
                if nm == r['name']:
                    r['descript'] = upddesc
                writer.writerow(r)

        shutil.move(temp_file.name, csv_file)

        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            temp_name = ''
            temp_descript1 = ''
            for r in csv_reader:
                if nm == r['name']:
                    temp_name = r['name']
                    temp_descript1 = r['descript']
                    break

            if temp_name != '' and temp_descript1 != '':
                return render_template('room.html', name=temp_name, description=temp_descript1, message="found")
            else:
                return render_template('room.html', error="Picture and Name did not find for Room!")


if __name__ == "__main__":
    app.run(debug=True)
