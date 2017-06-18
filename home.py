from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello_world():
    print("dasboard")
    return render_template('dashboard.html')

@app.route('/discrete')
def discrete():
    print("discrete")
    return render_template('discrete.html')

@app.route("/algorithms")
def algorithms():
    print("algorithms")
    return render_template('algorithms.html')

if __name__ == '__main__':
    app.run()
