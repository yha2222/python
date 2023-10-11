import pymysql

conn = pymysql.connect(
    host = 'localhost',
    port = 3305,
    database = 'python',
    user = 'root',
    password = 'python'
    )

e_id = '6'
e_name = '9'
gen = '9'
addr = '9'

curs = conn.cursor()
sql = f"""
            UPDATE emp
            SET
                e_name = '{e_name}',
                gen = '{gen}',
                addr = '{addr}'
            WHERE
                e_id = '{e_id}'
     """
print(sql)

curs.execute(sql)
print("cnt", curs.rowcount)
conn.commit()

curs.close()
conn.close()