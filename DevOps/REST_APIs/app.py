from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def home():
    day = datetime.today().strftime("%A")
    time = datetime.today().strftime("%H:%M:%S")
    # print(time)
    return render_template('index.html', time=time, day=day)

@app.route('/api')
def func():
    name = request.values.get('name')
    age = request.values.get('age')
    result = {
        'name': name,
        'age': age
    }
    return result

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = dict(request.form)
    return data

if __name__ == '__main__':
    app.run(debug=True)