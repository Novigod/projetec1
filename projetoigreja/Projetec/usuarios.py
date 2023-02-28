import banco
from flask import render_template
from flask import Flask, request, redirect, session, flash, url_for


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


def lista_usuarios ():
    conn = banco.banco_connect()
    lista_usuarios = conn.execute("select * from usuarios").fetchall()
    conn.close()
    return lista_usuarios



def add(request):
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    valido = valido_user(tag, email, senha)
    conn = banco.banco_connect()
    banco.banco_cursor(conn, f""" insert into users (nome, email, senha, verificado) values
    ('{nome}', '{email}', '{senha}', 0)""")
    conn.close()
    return [valido,email]

def valido_user(nome, email, senha):
    if tag == "" or email == "" or senha == "":
        return "Um dos campos está  vazio "
    
    if tag.count(";") > 0 or email.count(";") > 0 or senha.count(";") > 0:
        return 'Caractere inválid: ;'
    
    if buscar_user(email):
        return "E-mail já cadastrado"
    return None

def login_user(request):
    email = request.form['email']
    senha = request.form['senha']

    user = buscar_user(email)
    if user:
        if user['senha'] ==  senha:
            return email
    return False

def buscar_user(email):
    for x in lista_usuarios():
        if x['email'] == email:
            return x
    return None

