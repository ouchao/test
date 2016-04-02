#coding=utf-8
import MySQLdb.cursors
import MySQLdb
import re


class mysql_crud():

    def __init__(self):
        self.conn= MySQLdb.connect(
                host    ='192.168.1.64',
                port    = 3306,
                user    ='root',
                passwd  ='rootroot',
                db      ='seo',
                cursorclass = MySQLdb.cursors.DictCursor,
                )
        self.prefix = 'b2bvip_'
        self.suffix = '_sum'
        self.cur    = self.conn.cursor()

    #创建数据表
    def create_table(self,table,field_setting):
        self.cur.execute("create %s table(%s)"%(table,field_setting))

    def count(self,table):
        self.cur.execute("select count(*) from %s;"%(table))

    #插入一条数据
    def insert_row(self,table,data):
        #self.cur.execute("insert into student values('2','Tom','3 year 2 class','9')")
        #print("insert into %s values%s"%(table,data))
        self.cur.execute("insert into %s values%s"%(table,data))

    #修改查询条件的数据
    def update_row(self):
        self.cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

    #删除查询条件的数据
    def delete_row(self):
        self.cur.execute("delete from student where age='9'")

    def get_fields(self):
        fields = self.cur.execute("SHOW COLUMNS FROM b2bvip_member_sum")
        for field in cur.fetchmany(member_fields):
            print field



mysql=mysql_crud()

with open('13.log','r') as LOG:
    for line in LOG.readlines():
        try:
            datal=line.split('|')
            datal[5]=datal[5].replace('T',' ').replace('+08:00','').strip()
            tmp=re.split('\s+',datal[7].strip())
            datal[7]=tmp[1]
            datal.append(tmp[0])
            datal.append(tmp[2])
            datal.insert(0,'')
            datal=map(lambda a: a.strip(),datal)

            sqldata=tuple(datal)
            mysql.insert_row('seo',str(sqldata))
        except Exception,e:
            with open('error.log','a') as ERR:
                ERR.write("err:%s\n"%(str(e)))
                ERR.write("%s\n\n"%(line))


