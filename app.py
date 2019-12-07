from flask import Flask
from flask import render_template
app = Flask(__name__, static_url_path='/templates')


@app.route('/')
def hello_world():
    return render_template('unauthorised.html', found='yes')


@app.route('/auth')
def auth():
    return render_template('authorised.html', username='Pavel')


if __name__ == '__main__':
    app.run()
