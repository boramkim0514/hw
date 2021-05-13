## mysql 연동
import pymysql as my

con = my.connect(host='127.0.0.1', user='root', password='25722357', db='mydb')
c = con.cursor()

c.execute('insert into movie values("명량", "최민식", 1761)') 
c.execute('update movie set actor="김혜수" where title = "도둑들" ')
c.execute('delete from movie where title = "광해" ')

c.execute('select * from movie')

res = c.fetchall()

print('*********************')
print('movie actor audience')
print('*********************')

for i in res:
    print(i[0], i[1], i[2])    
print('*********************')

con.commit()
c.close()

con.close()


