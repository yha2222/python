import pymysql

conn = pymysql.connect(
    host = 'localhost',
    port = 3305,
    database = 'python',
    user = 'root',
    password = 'python'
    )

# jdbc - st
cursor = conn.cursor(pymysql.cursors.DictCursor)

sql="SELECT * FROM emp"
cursor.execute(sql)

all = cursor.fetchall() # jdbc - rs
print(all)

cursor.close()
conn.close()