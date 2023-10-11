import pymysql
class DaoMember:
    def __init__(self):
        self.conn = pymysql.connect(
                    host = 'localhost',
                    port = 3305,
                    database = 'python',
                    user = 'root',
                    password = 'python'
                    )

        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def selectList(self):
        sql="SELECT * FROM member"
        self.curs.execute(sql)
        
        members = self.curs.fetchall()
        return members
    
    def selectOne(self, m_id):
        sql=f"""
            SELECT
                m_id, m_name, tel, email
            FROM member
            WHERE m_id = '{m_id}'
            """
        self.curs.execute(sql)
        member = self.curs.fetchone()
        return member
    
    def insert(self, m_name, tel, email):
        sql = f"""
            INSERT INTO member
                (m_name, tel, email)
            VALUES
                ('{m_name}', '{tel}', '{email}')
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def update(self, m_id, m_name, tel, email):
        sql = f"""
            UPDATE member
            SET
                m_name = '{m_name}',
                tel = '{tel}',
                email = '{email}'
            WHERE
                m_id = '{m_id}'
            """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self, m_id):
        sql = f"""
            DELETE
            FROM member
            WHERE
                m_id = '{m_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()

if __name__ == '__main__':
    dm = DaoMember()
    cnt = dm.delete('5')
    print("cnt", cnt)