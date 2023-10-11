import pymysql

conn = pymysql.connect(
    host = 'localhost',
    port = 3305,
    database = 'python',
    user = 'root',
    password = 'python'
    )

# jdbc - st
curs = conn.cursor(pymysql.cursors.DictCursor)

sql="SELECT * FROM emp"
curs.execute(sql)

rows = curs.fetchall() # jdbc - rs
print(rows)

curs.close()
conn.close()