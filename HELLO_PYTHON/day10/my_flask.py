from flask import Flask,render_template
from flask.globals import request
import pymysql
from day10.daomember import DaoMember
app = Flask(__name__)

@app.route('/')
@app.route('/member_list')
def member_list():
    dm = DaoMember()
    members = dm.selectList()
    return render_template('member_list.html', members = members)

@app.route('/member_add')
def member_add():
    return render_template('member_add.html')

@app.route('/member_add_act', methods=['POST'])
def member_add_act():
    m_name = request.form['m_name']
    tel = request.form['tel']
    email = request.form['email']

    dm = DaoMember()
    cnt = dm.insert(m_name, tel, email)
    return render_template('member_add_act.html', cnt = cnt)

@app.route('/member_detail')
def member_detail():
    m_id = request.args.get('m_id')
    dm = DaoMember()
    vo = dm.selectOne(m_id)
    return render_template('member_detail.html', vo = vo)

@app.route('/member_mod')
def member_mod():
    m_id = request.args.get('m_id')
    dm = DaoMember()
    vo = dm.selectOne(m_id)
    return render_template('member_mod.html', vo = vo)

@app.route('/member_mod_act', methods=['POST'])
def member_mod_act():
    m_id = request.form['m_id']
    m_name = request.form['m_name']
    tel = request.form['tel']
    email = request.form['email']

    dm = DaoMember()
    cnt = dm.update(m_id, m_name, tel, email)

    return render_template('member_mod_act.html', cnt = cnt)

@app.route('/member_del_act', methods=['POST'])
def member_del_act():
    m_id = request.form['m_id']
    dm = DaoMember()
    cnt = dm.delete(m_id)
    return render_template('member_del_act.html', cnt = cnt)

if __name__ == '__main__':
    app.run(debug=True)