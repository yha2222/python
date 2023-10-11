import pymysql

class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(
                host = 'localhost',
                user = 'root',
                password = 'python',
                db = 'python',
                charset = 'utf8',
                port = 3305
                )
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def selectList(self):
        sql="SELECT * FROM emp"
        self.curs.execute(sql)
        list = self.curs.fetchall()
        return list
    
    def selectOne(self, e_id):
        sql = f"""
            SELECT
                e_id,e_name,gen,addr
            FROM emp
            WHERE
                e_id = '{e_id}'
        """
        self.curs.execute(sql)
        vo = self.curs.fetchone()
        return vo
    
    def insert(self,e_id,e_name,gen,addr):
        sql = f"""
            INSERT INTO emp
                (e_id, e_name, gen, addr)
            VALUES
                ('{e_id}', '{e_name}', '{gen}', '{addr}')
        """
        self.curs.execute(sql)
        self.conn.commit()
        return self.curs.rowcount
    
    def update(self,e_id,e_name,gen,addr):
        sql = f"""
            UPDATE emp
            SET
                e_name = '{e_name}',
                gen = '{gen}',
                addr = '{addr}'
            WHERE
                e_id = '{e_id}'
            """
        self.curs.execute(sql)
        self.conn.commit()
        return self.curs.rowcount
    
    def delete(self, e_id):
        sql = f"""
            DELETE
            FROM emp
            WHERE
                e_id = '{e_id}'
        """
        self.curs.execute(sql)
        self.conn.commit()
        return self.curs.rowcount
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoEmp()
    cnt = de.selectOne('1')
    print("cnt", cnt)