from flask import Flask,render_template
from flask.globals import request
from flask.json import jsonify
from day09 import daoemp
from day12.daoemp import DaoEmp
app = Flask(__name__)

@app.route('/')
def root():
    return 'Hello Ha'

@app.route('/emp_selects', methods=['POST'])
def emp_selects():
    de = DaoEmp()
    list = de.selectList()
    return jsonify({'list': list})

@app.route('/emp_select', methods=['POST'])
def emp_select():
    e_id = request.form['e_id']
    de = DaoEmp()
    vo = de.selectOne(e_id)
    return jsonify({'vo': vo})

@app.route('/emp_add', methods=['POST'])
def emp_add():
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    gen = request.form['gen']
    addr = request.form['addr']
    
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, gen, addr)
    return jsonify({'cnt': cnt})

@app.route('/emp_mod', methods=['POST'])
def emp_mod():
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    gen = request.form['gen']
    addr = request.form['addr']
    
    de = DaoEmp()
    cnt = de.update(e_id, e_name, gen, addr)
    return jsonify({'cnt': cnt})

@app.route('/emp_del', methods=['POST'])
def emp_del():
    e_id = request.form['e_id']
    
    de = DaoEmp()
    cnt = de.delete(e_id)
    return jsonify({'cnt': cnt})

@app.route('/myajax', methods=['POST', 'GET'])
def myajax():
    menu = request.form['menu']
   # menu = request.args.get('menu')
    print("menu", menu)
    return jsonify({'msg': 'hello'})

@app.route('/myajax_axios', methods=['POST', 'GET'])
def myajax_axios():
    params = request.get_json()
    print("params", params['menu'])
    return jsonify({'msg': 'hello'})

if __name__ == '__main__':
    app.run(debug=True)