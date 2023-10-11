from flask import Flask,render_template
from flask.globals import request
import pymysql
app = Flask(__name__)

@app.route('/')
def root():
    return 'Hello Ha'

@app.route('/param')
def param():
    menu = request.args.get('menu')
    return 'param:'+menu

@app.route('/post',methods=['POST','GET'])
def post():
    menu = request.form.get('menu')
    # menu = request.form['menu']
    return 'post:'+menu

@app.route('/forw', methods=['GET','POST'])
def forw():
    a = '홍길동'
    b = ['전우치', '이순신', '유관순']
    c = [
        {'e_id':1, 'e_name':1, 'gen':1, 'addr':1,},
        {'e_id':2, 'e_name':2, 'gen':2, 'addr':2,},
        {'e_id':3, 'e_name':3, 'gen':3, 'addr':3,}
    ]
    
    return render_template('forw.html', a = a, b = b, c = c ) #request.setAttribute("a", a);

@app.route('/emp')
def emp():
    conn = pymysql.connect(
    host = 'localhost',
    port = 3305,
    database = 'python',
    user = 'root',
    password = 'python'
    )
    
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    sql="SELECT * FROM emp"
    cursor.execute(sql)
    
    emps = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('emp.html', emps = emps)

if __name__ == '__main__':
    app.run(debug=True)