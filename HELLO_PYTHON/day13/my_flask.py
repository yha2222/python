from flask import Flask, redirect
from flask.globals import request
from flask.json import jsonify
from day13.daomember import DaoMember

app = Flask(__name__)

@app.route('/')
def member():
    return redirect("static/member.html")

@app.route('/mem_selects', methods=['POST'])
def mem_selects():
    dm = DaoMember()
    list = dm.selectList()
    return jsonify({'list': list})

@app.route('/mem_select', methods=['POST'])
def mem_select():
    params = request.get_json()
    m_id = params['m_id']
    de = DaoMember()
    vo = de.selectOne(m_id)
    return jsonify({'vo': vo})

if __name__ == '__main__':
    app.run(debug=True)