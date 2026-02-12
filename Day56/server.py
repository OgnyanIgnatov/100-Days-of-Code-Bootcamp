from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<name>')
def page(name):
    return render_template(f'{name}.html')

if __name__ == '__main__':
    app.run(debug=True)