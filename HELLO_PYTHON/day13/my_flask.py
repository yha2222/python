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
    dm = DaoMember()
    vo = dm.selectOne(m_id)
    return jsonify({'vo': vo})

@app.route('/mem_add', methods=['POST'])
def mem_add():
    params = request.get_json()
    m_name = params['m_name']
    tel = params['tel']
    email = params['email']
    
    dm = DaoMember()
    cnt = dm.insert(m_name, tel, email)
    return jsonify({'cnt': cnt})

@app.route('/mem_mod', methods=['POST'])
def mem_mod():
    params = request.get_json()
    m_id = params['m_id']
    m_name = params['m_name']
    tel = params['tel']
    email = params['email']
    
    dm = DaoMember()
    cnt = dm.update(m_id, m_name, tel, email)
    return jsonify({'cnt': cnt})

@app.route('/mem_del', methods=['POST'])
def mem_del():
    params = request.get_json()
    m_id = params['m_id']
    
    dm = DaoMember()
    cnt = dm.delete(m_id)
    return jsonify({'cnt': cnt})

if __name__ == '__main__':
    app.run(debug=True)