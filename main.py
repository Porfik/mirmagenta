from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/one')
def one():
    return render_template('one.html')


@app.route('/two')
def two():
    return render_template('two.html')


@app.route('/three')
def three():
    return render_template('three.html')


@app.route('/four')
def contacts():
    return render_template('four.html')


if __name__ == '__main__':
    app.run()
