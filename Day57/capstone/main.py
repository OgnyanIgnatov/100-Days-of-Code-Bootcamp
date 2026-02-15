from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://api.npoint.io/f0b2d2393c0baeaaee57')
    data = response.json()
    return render_template("index.html", data=data)

@app.route('/post/<int:id>')
def blog_post(id):
    response = requests.get('https://api.npoint.io/f0b2d2393c0baeaaee57')
    data = response.json()
    post = None
    for i in data:
        if i['id'] == id:
            post = i

    return render_template('post.html', post=post)

if __name__ == "__main__":
    app.run(debug=True)
