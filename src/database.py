import sqlite3

DB_NAME = 'inventory.db'

def connect_db():
    """Conecta ao banco de dados SQLite."""
    return sqlite3.connect(DB_NAME)

def init_db():
    """Inicializa o banco de dados criando a tabela, se necessário."""
    conn = connect_db()
    cursor = conn.cursor()

    # Cria a tabela se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantidade INTEGER NOT NULL
        )
    ''')

    # Verificar se a coluna 'quantidade' existe (para bancos antigos)
    try:
        cursor.execute('SELECT quantidade FROM items LIMIT 1')
    except sqlite3.OperationalError:
        print("Adicionando coluna 'quantidade' no banco existente...")
        cursor.execute('ALTER TABLE items ADD COLUMN quantidade INTEGER NOT NULL DEFAULT 0')
        conn.commit()

    conn.commit()
    conn.close()

def get_items():
    """Obtém todos os itens do banco de dados."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, quantidade FROM items')
    items = [{'id': row[0], 'name': row[1], 'quantidade': row[2]} for row in cursor.fetchall()]
    conn.close()
    return items

def add_item(name, quantidade):
    """Adiciona um novo item ao banco de dados."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO items (name, quantidade) VALUES (?, ?)', (name, quantidade))
    conn.commit()
    conn.close()

def delete_item(item_id):
    """Exclui um item pelo ID."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM items WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
