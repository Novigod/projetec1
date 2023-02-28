from flask import render_template
from flask import Flask, request, redirect, session, flash, g
import usuarios

app = Flask(__name__)
app.secret_key = 'opa'

@app.before_request
def carregar_email():
    if 'usuario_email' in session:
        g.user = usuarios.buscar_user(session['usuario_email'])


@app.route('/')
def home():
    return render_template('home.html', titulo="Home")


@app.route('/atv-metas')
def atv_metas():
    return render_template('atv_metas.html', titulo='Atividades')


@app.route('/qs')
def quem_somos():
    return render_template('qs.html', titulo='Quem Somos')


@app.route('/cadastrarUser', methods=(['POST', 'GET']))
def cadastropag():
    if request.method == 'POST':
        add = usuarios.add(request)
        if add[0]:
            flash(add[0])
            return redirect(url_for('cadastropag'))
        session["usuario_email"] =add[1]
        return redirect(url_for('home'))
    if 'user' in g:
        return redirect(url_for('perfil'))
    return render_template('cadastrarUser.html') 


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = usuarios.buscar(email, senha)
        if usuario is None:
            flash('Usuário/ Senha Inválidos.')
        else:
            session['usuario_email'] = usuario.email
            session['usuario_nome'] = usuario.nome
            return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/login', methods=(['POST', 'GET']))
def login():
    if request.method == 'POST':
        login = users.login_user(request)
        if login:
            session["usuario_email"] = login
            return redirect(url_for('home'))
        flash("E-mail e/ou Senha inválidos.")
    
    if 'user' in g:
        return redirect(url_for('perfil'))
    return render_template('login.html')


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('usuario_email', None)
    session.pop('usuario_nome', None)
    return redirect(url_for('index'))


def usuario_logado():
    return 'usuario_email' in session


@app.errorhandler(403)
def acesso_negado(erro):
    return render_template('acesso_negado.html', titulo='Ops!'), 403


@app.before_request
def carregar_usuario():
    if 'usuario_email' in session:
        g.usuario = usuarios.buscar_por_email(session['usuario_email'])


app.run(debug=True)


# em manutenção!!
