import pymysql

conn = pymysql.connect(host = 'localhost',user = 'root',password='hidden',db = 'pythontestdb')

mycursor = conn.cursor()

sql = 'INSERT into ninja(name,village,attack) VALUES (%s, %s ,%s)'

# To insert one row at a time...note that tuple is needed here
# ninja = ('Naruto', 'Konoha', 'Rasengan')
# mycursor.execute(sql,ninja)

# to inset multiple rows

ninja = [
  ('Naruto', 'Konoha', 'Rasengan'),
  ('Sasuke', 'Konoha', 'Chidori'),
  ('Shikamaru', 'Konoha', 'Shadow Possession Jutsu'),
  ('Gaara', 'Sand Village', 'Sand Coffin'),
]
mycursor.executemany(sql,ninja)

mycursor.execute('SELECT * from ninja')

conn.commit() # to commit the rows to the tables

print(mycursor.fetchall())