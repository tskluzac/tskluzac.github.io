from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def dashboard():
    print("dashboard")
    return render_template('dashboard.html')

@app.route('/research')
def research():
    print("research")
    return render_template('research.html')

@app.route("/blog")
def blog():
    print("blog")
    return render_template('blog.html')

if __name__ == '__main__':
    app.run()

