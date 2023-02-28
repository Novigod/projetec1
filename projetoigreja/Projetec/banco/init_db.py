
import sqlite3

connection = sqlite3.connect('projetec.db')

with open('banco/banco.sql') as banco:
    connection.executescript(banco.read())

cur = connection.cursor()
cur.execute("""insert into usuarios (nome, email, senha) values 
('user1', 'user1@gmail.com', '1234'), 
('user2', 'user2@gmail.com', '5678')""")

connection.commit()
connection.close()