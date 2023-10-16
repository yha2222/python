from flask import Flask,render_template
from flask.globals import request
import pymysql
app = Flask(__name__)

@app.route('/')
def root():
    return 'Hello Ha'

if __name__ == '__main__':
    app.run(debug=True)