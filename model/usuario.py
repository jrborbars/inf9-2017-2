# coding:utf8
import sqlite3
db = sqlite3.connect("model/Biblioteca.db")
cursor = db.cursor()

class Usuario():
	def __init__(self):
		self.table = "usuarios"

	def findAll(self):
		sql = "select id,nome from " + self.table
		return cursor.execute(sql)

	def findOne(self,_id_):
		sql = "select * from " + self.table + " where id = ?"
		cursor.execute(sql,(_id_))
		dados = cursor.fetchone()
		return dados

	def update(self,nome,email,_id_):
		sql = "update " + self.table + " set nome = ? , email = ? where id = ?"
		cursor.execute(sql,(nome,email,_id_))
		db.commit()

	def delete(self,_id_):
		sql = "delete from " + self.table + " where id = ?"
		cursor.execute(sql,(_id_))
		db.commit()

	def insert(self,nome,email,senha):
		sql = "insert into "+self.table+" (nome,email,senha) values (?,?,?)"
		cursor.execute(sql,(nome,email,senha))
		db.commit()

	def reset_pw():
		pass

	def check_user(self,email):
		sql = "SELECT email,senha FROM " + self.table + " WHERE email = ?"
		print(email)
		cursor.execute(sql,(email,))
		dado = cursor.fetchone()
		print(dado)
		return dado