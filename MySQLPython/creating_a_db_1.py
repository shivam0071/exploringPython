import pymysql

# Notice that no db name is used here
conn = pymysql.connect(host='localhost',user='root', password='hidden')

mycursor = conn.cursor()

# sql = 'CREATE DATABASE pythontestDB'
#
# mycursor.execute(sql)

mycursor.execute("SHOW DATABASES")

for db in mycursor:
  print(db)


#('information_schema',)
# ('mysql',)
# ('ninjaworld',)
# ('performance_schema',)
# ('pythontestdb',)
# ('sakila',)
# ('sys',)
# ('test_db1',)
# ('world',)

# the DB has been created :D