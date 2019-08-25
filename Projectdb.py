import datetime
import sqlite3 as sq
con=sq.connect('CafeDB.db')
cur=con.cursor()
d=datetime.datetime.now()
print(d)
cur.execute("CREATE TABLE Transac(customer text,items text,pay_method text,date text,transaction_id text,total_price real,amount_paid real,change real,reciept blob)")
con.commit()

print('table created')

con.close()