import pymysql

conn = pymysql.connect(
    host = 'localhost',
    port = 3305,
    database = 'python',
    user = 'root',
    password = 'python'
    )

e_id = '6'
e_name = '6'
gen = '6'
addr = '6'

curs = conn.cursor()
sql = f"""
INSERT INTO emp
    (e_id, e_name, gen, addr)
VALUES
    ('{e_id}', '{e_name}', '{gen}', '{addr}')
"""
print(sql)

cnt = curs.execute(sql)
print("cnt", cnt)
conn.commit()

curs.close()
conn.close()