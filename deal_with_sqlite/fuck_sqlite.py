import sqlite3
conn = sqlite3.connect('userDB.db')

conn.execute("create table if not exists address(id integer primary key autoincrement, name varchar(128), address varchar(128))")
conn.execute("insert into address(name, address) values('wangxiong' , 'best')")
conn.execute("insert into address(name, address) values('xiongwang', 'Wuhan')")

conn.commit()
cur = conn.cursor()
cur.execute("select * from address")

res = cur.fetchall()

print "address: ", res
for line in res:
    for f in line:
        print f

cur.close()
conn.close()

