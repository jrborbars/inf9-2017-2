import sqlite3
db = sqlite3.connect("model/Biblioteca.db")
cursor = db.cursor()

class Livro():
	def __init__(self):
		self.table = "livros"

	def findAll(self):
		sql = "select * from " + self.table
		cursor.execute(sql)
		return cursor.fetchall()

	def findOne(self,_id_):
		sql = "select * from " + self.table + " where id = ?"
		cursor.execute(sql,(_id_))
		dados = cursor.fetchone()
		return dados

	def update(self,titulo,autor,ano,editora,isbn,sinopse,sit,_id_):
		sql = "update " + self.table + " set titulo = ?,autor = ?,ano = ?,editora = ?,isbn = ?,sinopse = ? ,sit = ? where id = ?"
		cursor.execute(sql,(titulo,autor,ano,editora,isbn,sinopse,sit,_id_))
		db.commit()

	def delete(self,_id_):
		sql = "delete from " + self.table + " where id = ?"
		cursor.execute(sql,(_id_))
		db.commit()

	def insert(self,titulo,autor,ano,editora,isbn,sinopse,sit):
		sql = "insert into "+self.table+" (titulo,autor,ano,editora,isbn,sinopse,sit) values (?,?,?,?,?,?,?)"
		cursor.execute(sql,(titulo,autor,ano,editora,isbn,sinopse,sit))
		db.commit()