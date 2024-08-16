from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')  # Decorator que atribui uma função a uma rota
def home():
    return render_template('home.html')

@app.route('/cursos')
def cursos():
    return render_template('cursos.html')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

@app.route('/habilidades')
def habilidades():
    return render_template('habilidades.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/projeto1')
def projeto1():
    return render_template('projeto1.html')

@app.route('/projeto2')
def projeto2():
    return render_template('projeto2.html')

@app.route('/projeto3')
def projeto3():
    return render_template('projeto3.html')

@app.route('/projeto4')
def projeto4():
    return render_template('projeto4.html')

@app.route('/projeto5')
def projeto5():
    return render_template('projeto5.html')

if __name__ == '__main__':
    app.run(debug=True)

