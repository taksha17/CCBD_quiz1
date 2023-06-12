from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/name", methods=['GET', 'POST'])
def name():
    return render_template('Name.html')

@app.route("/namedisp", methods=['GET', 'POST'])
def namedisp():
    if request.method == 'POST':
        name = request.form['name']
        cnt = 0
        img_path = ''
        picn = ''
        csv_reader = csv.DictReader(open('static/names.csv'))
        for r in csv_reader:
            if name == r['Name']:
                img_path = 'static/' + r['Picture']
                picn = r['Picture']
                cnt += 1
        if cnt != 0:
            return render_template('Dispname.html', msg="Found", path=img_path, picn=picn)
        else:
            return render_template('Dispname.html', error="Name is not Found")

@app.route("/state", methods=['GET', 'POST'])
def name1():
    return render_template('State.html')

@app.route("/statedisp", methods=['GET', 'POST'])
def statedisp():
    if request.method == 'POST':
        state = request.form['state']
        cnt = 0
        name = list()
        pic = list()
        cap = list()
        csv_reader = csv.DictReader(open('static/names.csv'))
        for r in csv_reader:
            if r['State'] == state:
                name.append(r['Name'])
                pic.append('static/' + r['Picture'])
                cap.append(r['Caption'])
                cnt += 1

        last = (name, pic, cap)

        if cnt != 0:
            return render_template('Statedips.html', last=last,msg="found")
        else:
            return render_template('Statedips.html', error="Not Found")

@app.route("/room", methods=['GET', 'POST'])
def room():
    return render_template('Room.html')

@app.route("/roomdisp", methods=['GET', 'POST'])
def roomdisp():
    if request.method == 'POST':
        state = request.form['room']
        cnt = 0
        name = ''
        pic = ''
        picn = ''
        cap = ''
        csv_reader = csv.DictReader(open('static/names.csv'))
        for r in csv_reader:
            if r['Room'] == state:
                name = r['Name']
                pic = 'static/' + r['Picture']
                picn = r['Picture']
                cap = r['Caption']
                cnt += 1

        if cnt != 0:
            return render_template('Roomdips.html', name=name, pic=pic, cap=cap, picn=picn, msg="found")
        else:
            return render_template('Roomdips.html', error="Not Found")


@app.route("/newsearch", methods=['GET', 'POST'])
def room():
    return render_template('Newsearch.html')

@app.route("/newdisp", methods=['GET', 'POST'])
def roomdisp():
    if request.method == 'POST':
        key =




if __name__ == "__main__":
    app.run(debug=True)