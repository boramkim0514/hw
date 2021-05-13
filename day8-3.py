## mysql - 연동 
import pymysql as my 

#arg =" host='127.0.0.1', user='root', \password='25722357', db='bdb'"
con = my.connect(host='127.0.0.1', user='root', password='25722357', db='bdb')
c = con.cursor()

c.execute('create table lunch(menu char(20), price int)')
# c.execute('insert into lunch values("짜장면", 5000)')
# c.execute('insert into lunch values("비빔밥", 8000)')
# c.execute('insert into lunch values("돈까스", 7000)')

c.execute('select * from lunch')

res = c.fetchall()

#print(res[0])
#print(res[0][0], res[0][1])
#print(res[1][0], res[1][1])
#print(res[2][0], res[2][1])

print('************')
print('산이름   해발')
print('************')

for i in res:
    print(i[0], i[1])    
print('************')

#c.execute('reate table m2(m char(20), a int)')
c.

con.commit()
c.close()

con.close()