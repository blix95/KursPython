import csv
import sqlite3

#conn=sqlite3.connect('example.db')

#c=conn.cursor()

#c.execute('''CREATE TABLE stocks
            # (date text, trans text, symbol text, qty real, price real)''')

#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

#conn.commit()

#rows = c.execute("SELECT * from stocks")
#rows = c.fetchall()

#for row in rows:
    #print(row)
'''
symbol = ('RHAT',)
for row in c.execute('SELECT*FROM stocks WHERE symbol= ?',symbol):
    print(row)
    

zakupy=[
    ('2022-03-05','BUY','BMW',15,103000),
    ('2015-03-06','SELL','Volvo',17,250000),
    ('2016-10-05','BUY','OPEL',22,67000),
    ('2011-12-12','SELL','AUDI',19,124900),

]
'''
#c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)',zakupy)
#conn.commit()
#for row in c.execute('SELECT * FROM stocks WHERE trans="BUY" ORDER BY price DESC'):
#    print(row)
"""
c.execute('''CREATE TABLE users
            (id real,name text, surname text)''')
c.execute("INSERT INTO users VALUES(1, 'Wojtek', 'Klimaszewski')''')

conn.commit()


osoby=[
    (2,'Kamil','Ślimak'),
    (3,'Klara','Sobieraj'),
    (4,'Krzysztof','Stanowski'),
    (5,'Marcin','Najman'),
]

#c.executemany('INSERT INTO users VALUES (?,?,?)',osoby)
#conn.commit()

for row in c.execute('SELECT*FROM users ORDER BY id DESC'):
    print(row)

"""
#conn=sqlite3.connect('CodeBrainers.db')

#c=conn.cursor()

#for row in c.execute("SELECT*FROM customer"):
   # print(row)
#c.execute('''CREATE TABLE Companies
   #         (id real,name text, city text,date_create text)''')
#conn.commit()

#c.execute("INSERT INTO companies VALUES (1,'Apple','California','01-10-1995')",)
#conn.commit()

#for row in c.execute("SELECT*FROM companies"):
  #  print(row)

