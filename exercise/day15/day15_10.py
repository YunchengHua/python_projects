'''

class Exc:
    def __init__(self, host, port, db, charset):
        self.host = host
        self.port = port
        self.db = db
        self.charset = charset

    def exc1(self,operation):
        conn = connect(self.host, self.port, self.db, self.charset,operation)
        conn.execute(sql)
        return xxx

    def exc2(self,pro_name):
        conn = connect(self.host, self.port, self.db, self.charset,pro_name)
        conn.call_proc(sql)
        return xxx


mySql = Exc('127.0.0.1',3306,'db1','utf8')
mySql.exc1('select * from tb1;')
mySql.exc2('存储过程的名字')

'''