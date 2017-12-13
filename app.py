# coding:utf8
from bottle import *
import bcrypt
import beaker.middleware 
#import SessionMiddleware
from model.usuario import Usuario
from model.livro import Livro
import sqlite3

session_opts = {
	'session.key' :	'ETEMMMINF9',
	'session.type': 'memory',
	'session.cookie_expires': 600,
	'session.auto' : True}
	
app = beaker.middleware.SessionMiddleware(app(),session_opts)

@route('/static/<filename:re:.*\.css>')
def static_css(filename):
	return static_file(filename, root='static/css')

@route('/static/<filename:re:.*\.js>')
def static_js(filename):
	return static_file(filename, root='static/js')

@route('/static/<filename:re:.*\.(jpg|png|gif|ico)>')
def static_img(filename):
    return static_file(filename, root='static/img')
    
@error(404)
def error404(error): 
    return template('view/error.tpl')

@route('/login', method = "GET")
def login_get():
	return template('view/login.tpl')

@route('/login', method = "POST")
def login_post():
	email = str(request.POST.email)
	print(type(email))
	senha = request.POST.senha
	dado = Usuario().check_user(email)
	senhah = dado[1]		
	if(bcrypt.hashpw(senha.encode(),senhah.encode()) == dado[1]):
		_session_ = request.environ['beaker.session']
		print(type(_session_))
		_session_["usuario"] = dado[0]
		_session_.save()
		return redirect("/")
	else:
		print("Dados incorretos")


@route('/list')
def list_all():
	dados = Usuario().findAll()
	return template('view/list.tpl',dados=dados)

@route('/list_book')
def list_book_all():
	dados = Livro().findAll()
	return template('view/list_book.tpl',dados=dados)

@route('/', method = "GET")
def index():
	return template('view/index.tpl')

@route('/insert', method='GET')
def insert_get():
    return template('view/insert.tpl')
@route('/insert_book', method='GET')
def insert_get_book():
    return template('view/insert_book.tpl')

@route('/update/<_id_>', method='GET')
def update_get(_id_):
	dados = Usuario().findOne(_id_)
	return template('view/update.tpl', dados=dados)

@route('/update_book/<_id_>', method='GET')
def update_get_book(_id_):
	dados = Livro().findOne(_id_)
	return template('view/update_book.tpl', dados=dados)

@route('/delete/<_id_>', method = 'GET')
def delete_get(_id_):	
	dados = Usuario().findOne(_id_)
	return template('view/delete.tpl', dados=dados)
@route('/delete_book/<_id_>', method = 'GET')
def delete_get_book(_id_):	
	dados = Livro().delete(_id_)
	return redirect("/list_book")

@route('/profile/<_id_>', method = 'GET')
def profile_get(_id_):
	dados = Usuario().findOne(_id_)
	return template('view/profile.tpl', dados=dados)

@route('/insert', method='POST')
def insert_post():
    nome = request.POST.nome.strip()
    email = request.POST.email.strip()
    senha = request.POST.senha.strip()
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(senha.encode("utf-8"),salt)
    Usuario().insert(nome,email,hashed)
    return redirect('/list')

@route('/insert_book', method='POST')
def insert_post_book():
    autor = request.POST.autor.strip()
    titulo = request.POST.titulo.strip()
    isbn = request.POST.isbn.strip()
    editora = request.POST.editora.strip()
    ano = request.POST.ano.strip()
    sit = request.POST.sit.strip()
    sinopse = request.POST.sinopse.strip()
    Livro().insert(titulo,autor,ano,editora,isbn,sinopse,sit)
    return redirect('/list_book')

@route('/update/<_id_>', method = 'POST')
def update_post(_id_):
	nome = request.POST.nome.strip()
	email = request.POST.email.strip()
	Usuario().update(nome,email,_id_)
	return redirect("/list")
@route('/update_book/<_id_>', method = 'POST')
def update_post_book(_id_):
	autor = request.POST.autor.strip()
	titulo = request.POST.titulo.strip()
	isbn = request.POST.isbn.strip()
	editora = request.POST.editora.strip()
	ano = request.POST.ano.strip()
	sit = request.POST.sit.strip()
	sinopse = request.POST.sinopse.strip()
	Livro().update(titulo,autor,ano,editora,isbn,sinopse,sit,_id_)
	return redirect("/list_book")


@route('/delete/<_id_>', method = 'POST')
def delete_post(_id_):	
	Usuario().delete(_id_)
	return redirect('/list')
       
run(host='localhost',port='8000',debug=True, reloader=True, app = app)
