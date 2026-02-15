from flask import Flask, render_template
import datetime, requests
app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.date.today().year
    return render_template('index.html', present_year=year)

@app.route('/guess/<name>')
def guess(name):
    gender_raw_data = requests.get(f'https://api.genderize.io/?name={str.lower(name)}')
    gender_data = gender_raw_data.json()
    age_raw_data = requests.get(f'https://api.agify.io?name={str.lower(name)}')
    age_data = age_raw_data.json()

    formatted_name = str.capitalize(name)
    gender = gender_data['gender']
    age = age_data['age']

    return render_template('guessing.html', name = formatted_name, gender=gender, age=age)

@app.route('/blog')
def blog():
    response = requests.get('https://api.npoint.io/f0b2d2393c0baeaaee57')
    data = response.json()
    
    return render_template('blog.html', data=data)


if(__name__ == '__main__'):
    app.run(debug=True)