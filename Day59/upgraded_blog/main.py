from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/cd1db2ddbb2c901fac6a")
    data = response.json()

    return render_template("index.html", data=data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:id>')
def post(id):
    response = requests.get("https://api.npoint.io/cd1db2ddbb2c901fac6a")
    data = response.json()
    post = None

    for i in data:
        if i['id'] == id:
            post = i

    return render_template('post.html', post=post)



if __name__ == '__main__':
    app.run(debug=True)