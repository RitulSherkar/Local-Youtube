from flask import Flask ,session, url_for,redirect, request
import os

from flask.templating import render_template
app = Flask(__name__, static_folder='static')

l = os.listdir('D:/Code/flask server/static')

@app.route('/')
def bruh():
    return render_template ('index.html', l = l)

@app.route('/test')
def test():
    return render_template ('test.html')


@app.route('/video/<name>')
def wow(name):
    return render_template('video.html', l = l, name = name)


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')