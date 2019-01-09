# cmd
# mysql -u root -p
# pip install pymysql

# starting the server service
  # net start MYSQL80
import pymysql

# 1.) Connect to a database using host, user, pass and db
conn = pymysql.connect(host='localhost',user='root', password='hidden',db ='ninjaworld')

#2.) Create a cursor that we can use to query on tables
a = conn.cursor()

# 3.) A SQL query
sql = 'SELECT * from villages'

#4) Execute the Query
a.execute(sql)

#5.) Work with the result of executed Query
data = a.fetchall()


print(data)

