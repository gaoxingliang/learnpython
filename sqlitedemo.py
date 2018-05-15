import sqlite3 as sq
# https://docs.python.org/3/library/sqlite3.html?highlight=sqlite
con = sq.connect("test.db")

c = con.cursor()
c.execute("create table if not exists username (user text, score int)")
c.execute("insert into username values ('u1', 1)")
c.execute("insert into username values ('u2', 23)")
# select
c.execute("select * from username where score > 0")
x = c.fetchone()
for t in c.fetchall():
    #print("user " + t[0])
    print("user %s got score %2d" % (t[0], t[1]));
con.commit()
con.close()
