from flask import Flask, render_template, request, redirect, url_for
from database import init_db, get_items, add_item, delete_item

app = Flask(__name__)

# Inicializa o banco de dados ao iniciar o app
init_db()

@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items=items)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form.get('nome')
    quantidade = request.form.get('quantidade')

    if nome and quantidade:
        try:
            quantidade = int(quantidade)
            add_item(nome, quantidade)
        except ValueError:
            pass  # quantidade inválida, ignora

    return redirect(url_for('index'))

@app.route('/excluir/<int:item_id>')
def excluir(item_id):
    delete_item(item_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
