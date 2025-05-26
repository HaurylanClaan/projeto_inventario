from flask import Flask, render_template, request, redirect, url_for
from database import init_db, get_items, add_item, delete_item, get_item, update_item
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Inicializa o banco de dados ao iniciar o app
init_db()

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return redirect(url_for('produtos'))

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        categoria = request.form.get('categoria')
        preco = request.form.get('preco')
        quantidade = request.form.get('quantidade')
        foto = request.files.get('foto')

        if nome and quantidade:
            try:
                quantidade = int(quantidade)
                preco = float(preco) if preco else 0.0
                if preco < 0:
                    preco = 0.0  # ou retorne um erro/mensagem para o usuário
                foto_filename = None
                if foto and foto.filename:
                    foto_filename = secure_filename(foto.filename)
                    foto.save(os.path.join(app.config['UPLOAD_FOLDER'], foto_filename))
                add_item(nome, quantidade, descricao, categoria, preco, foto_filename)
            except ValueError:
                pass  # valores inválidos

        return redirect(url_for('index'))
    return render_template('adicionar.html')

@app.route('/excluir/<int:item_id>')
def excluir(item_id):
    delete_item(item_id)
    return redirect(url_for('index'))

@app.route('/visualizar/<int:item_id>')
def visualizar(item_id):
    item = get_item(item_id)
    if not item:
        return "Produto não encontrado", 404
    return render_template('visualizar.html', item=item)

@app.route('/editar/<int:item_id>', methods=['GET', 'POST'])
def editar(item_id):
    item = get_item(item_id)
    if not item:
        return "Produto não encontrado", 404

    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        categoria = request.form.get('categoria')
        preco = request.form.get('preco')
        quantidade = request.form.get('quantidade')

        if nome and quantidade:
            try:
                quantidade = int(quantidade)
                preco = float(preco) if preco else 0.0
                if preco < 0:
                    preco = 0.0  # ou retorne um erro/mensagem para o usuário
                update_item(item_id, nome, descricao, categoria, preco, quantidade)
            except ValueError:
                pass  # valores inválidos

        return redirect(url_for('index'))

    return render_template('editar.html', item=item)

@app.route('/produtos')
def produtos():
    items = get_items()
    return render_template('produtos.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
