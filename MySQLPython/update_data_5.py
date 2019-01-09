import pymysql

conn = pymysql.connect(host = 'localhost',user = 'root',password='hidden',db = 'pythontestdb')

mycursor = conn.cursor()

# sql = "UPDATE ninja SET attack='Shadow Clone Jutsu' where name = 'Naruto'"
# mycursor.execute(sql)
# conn.commit()

mycursor.execute("SELECT * from ninja where name='Naruto'")
print(mycursor.fetchall())

# FROM RASENGAN to Shadow CLone Jutsu