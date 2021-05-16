
#1-4번*********************************************
## mysql 연동
import pymysql as my

con = my.connect(host='127.0.0.1', user='root', password='****', db='mydb')
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


** 6-7번 **************************************************************
import pymysql as my

con = my.connect(host='127.0.0.1', user='root', password='25722357', db='mydb')
c = con.cursor()

c.execute('create table Man(name char(20), age int)')
c.execute('insert into Man values("김연아", 32)') 
c.execute('insert into Man values("손흥민", 30)') 
c.execute('insert into Man values("이강인", 21)')

con.commit()
c.close()

con.close()

======================================================

mysql> insert into Man values('김연아', 32);
Query OK, 1 row affected (0.01 sec)

mysql> insert into Man values('손흥민', 30);
Query OK, 1 row affected (0.01 sec)

mysql> insert into Man values('이강인', 21);
Query OK, 1 row affected (0.01 sec)

mysql> select * from Man;
+--------+------+
| name   | age  |
+--------+------+
| 김연아 |   32 |
| 손흥민 |   30 |
| 이강인 |   21 |
+--------+------+
3 rows in set (0.00 sec)


