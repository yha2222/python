import pymysql

conn = pymysql.connect(
    host = 'localhost',
    port = 3305,
    database = 'python',
    user = 'root',
    password = 'python'
    )


curs = conn.cursor()
sql = """
INSERT INTO emp
    (e_id, e_name, gen, addr)
VALUES
    (%s, %s, %s, %s)
"""

curs.execute(sql, ('3', '3', '3', '3'))

conn.commit()

print(curs.rowcount, "record inserted.")

curs.close()
conn.close()