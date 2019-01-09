import pymysql

def printall(exec):
  for item in exec:
    print(item)
  print('*'*30)
conn = pymysql.connect(host='localhost',user = 'root', password = 'hidden',db = 'pythontestdb')

mycursor = conn.cursor()

sql1 = "SELECT name from ninja"
mycursor.execute(sql1)
printall(mycursor)

# notice the '' used in Konoha
sql2 = "SELECT * from ninja WHERE village='Konoha'"
mycursor.execute(sql2)
printall(mycursor)

sql3 = "SELECT village from ninja WHERE village LIKE '%no%'"
mycursor.execute(sql3)
printall(mycursor)

sql4 = "SELECT * from ninja WHERE name= %s"
mycursor.execute(sql4,('Naruto',))
printall(mycursor)

sql5 = "SELECT * from ninja LIMIT 2"
mycursor.execute(sql5)
printall(mycursor)

# LIMIT limits the number of results output

sql6 = "SELECT * from ninja LIMIT 2 offset 2"
mycursor.execute(sql6)
printall(mycursor)

# OFFSET  - offset shows the data after 2 rows in the db

