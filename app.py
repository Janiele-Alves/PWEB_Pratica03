from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('paginas/index.html')
 

@app.route('/listProdut')
def sobre():
    return render_template('paginas/listProdut.html')

@app.route('/descProduto')
def descricaoProduto():
    return render_template('paginas/descProduto.html')

@app.route('/carrinho')
def carrinho():
    return render_template('paginas/carrinho.html')

@app.route('/confirmacao')
def confriamacao():
    return render_template('paginas/confirmacao.html')

if __name__ == '__main__':
    app.run(debug=True)
