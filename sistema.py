import cgi


users = {
    '114269891483': 'caio',

}


form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')

if username in users and password == users[username]:
    # Credenciais corretas, redirecionar para a página restrita
    print("Location: pagina_restrita.html")
    print("Content-type: text/html\n")
else:
    # Credenciais incorretas, exibir mensagem de erro
    print("Content-type: text/html\n")
    print("Credenciais inválidas. Tente novamente.")
    