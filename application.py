from flask import Flask, render_template
from flask_bootstrap import Bootstrap


application = Flask(__name__)
Bootstrap(application)


@application.route('/')
def dashboard():
    print("dashboard")
    return render_template('dashboard.html')


@application.route('/research')
def research():
    print("research")
    return render_template('research.html')


@application.route("/blog")
def blog():
    print("blog")
    return render_template('blog.html')


if __name__ == '__main__':
    app.run()

