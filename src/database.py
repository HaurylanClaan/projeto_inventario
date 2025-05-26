import sqlite3
from datetime import datetime

DB_PATH = 'inventario.db'

def connect_db():
    """Conecta ao banco de dados SQLite."""
    return sqlite3.connect(DB_PATH)

def init_db():
    """Inicializa o banco de dados criando a tabela, se necessário."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS itens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER,
            descricao TEXT,
            categoria TEXT,
            preco REAL,
            foto TEXT,
            data_adicionado TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_item(nome, quantidade, descricao, categoria, preco, foto_filename):
    """Adiciona um novo item ao banco de dados."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        INSERT INTO itens (nome, quantidade, descricao, categoria, preco, foto, data_adicionado)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (nome, quantidade, descricao, categoria, preco, foto_filename, datetime.now().strftime('%Y-%m-%d')))
    conn.commit()
    conn.close()

def get_items():
    """Obtém todos os itens do banco de dados."""
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT id, nome, descricao, categoria, preco, quantidade, data_adicionado FROM itens')
    rows = c.fetchall()
    conn.close()
    items = []
    for row in rows:
        items.append({
            'id': row[0],
            'name': row[1],
            'descricao': row[2] or '',
            'categoria': row[3] or '',
            'preco': row[4] or 0.0,
            'quantidade': row[5],
            'data_adicionado': row[6]
        })
    return items

def delete_item(item_id):
    """Exclui um item pelo ID."""
    conn = connect_db()
    c = conn.cursor()
    c.execute('DELETE FROM itens WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()

def get_item(item_id):
    """Obtém um item pelo ID."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT id, nome, descricao, categoria, preco, quantidade, foto, data_adicionado FROM itens WHERE id = ?', (item_id,))
    row = c.fetchone()
    conn.close()
    if row:
        return {
            'id': row[0],
            'name': row[1],
            'descricao': row[2] or '',
            'categoria': row[3] or '',
            'preco': row[4] or 0.0,
            'quantidade': row[5],
            'foto': row[6],
            'data_adicionado': row[7]
        }
    return None

def update_item(item_id, nome, descricao, categoria, preco, quantidade):
    """Atualiza os detalhes de um item existente."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        UPDATE itens
        SET nome=?, descricao=?, categoria=?, preco=?, quantidade=?
        WHERE id=?
    ''', (nome, descricao, categoria, preco, quantidade, item_id))
    conn.commit()
    conn.close()
