import sqlite3 as s

con = s.connect('c:\\dd\\mydb')
c = con.cursor()

c.execute('insert into Man values("김연아", 32)')
c.execute('insert into Man values("손흥민", 30)')
c.execute('insert into Man values("이강인", 21)')
c.execute('select * from Man')


res = c.fetchall()

print(res)

con.commit()
con.close()