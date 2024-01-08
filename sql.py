import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('create table if not exists client(nom text,prenom text)')
c.execute("insert into client (nom , prenom) values ('RAVELOSON','ANDRITIANA MICHEL')")
c.execute("insert into client (nom , prenom) values ('RAVELOSON','ANDRITIANA DANIEL')")
results = c.execute("select * from client")
for i in results:
    print(i)
conn.commit()
c.close()
