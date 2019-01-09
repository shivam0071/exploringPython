import pymysql

# db added
conn = pymysql.connect(host='localhost',user='root', password='hidden')
mycursor = conn.cursor()

sql = 'CREATE TABLE ninja(name varchar(20), village varchar(20),attack varchar(50))'

mycursor.execute(sql)

mycursor.execute('SHOW TABLES')

for tables in mycursor:
  print(tables)


# OUTPUT:-
# ('ninja',)

# the table has been created in the database