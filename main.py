from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/main')
def index():
    return render_template('main.html')


@app.route('/data')
def one():
    return render_template('data.html')


@app.route('/pictures')
def two():
    return render_template('pictures.html')


@app.route('/goals')
def three():
    return render_template('goals.html')


@app.route('/about-us')
def contacts():
    return render_template('about-us.html')


if __name__ == '__main__':
    app.run()
