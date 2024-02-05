from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Página de Login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Aqui você pode adicionar a lógica para verificar as credenciais
        return "Login realizado com sucesso!"
    return render_template_string(html_login_form)

# Página de Registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Aqui você pode adicionar a lógica para registrar o usuário
        return "Registro realizado com sucesso!"
    return render_template_string(html_register_form)

html_login_form = '''
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form method="post">
        Nome de Usuário: <input type="text" name="username"><br>
        Senha: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    <p><a href="{{ url_for('register') }}">Não tem conta? Registrar</a></p>
</body>
</html>
'''

html_register_form = '''
<!DOCTYPE html>
<html>
<head>
    <title>Registrar</title>
</head>
<body>
    <h2>Registrar</h2>
    <form method="post">
        Nome de Usuário: <input type="text" name="username"><br>
        Senha: <input type="password" name="password"><br>
        <input type="submit" value="Registrar">
    </form>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
