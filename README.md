# Projeto Inventário

Este projeto é uma aplicação web para gerenciar um inventário utilizando Python e SQLite. Abaixo estão as instruções para configuração e uso.

## Estrutura do Projeto

```
projeto_inventario
├── static
│   └── styles.css         # Estilos CSS para a aplicação web
├── templates
│   └── index.html         # Template HTML principal da aplicação
├── src
│   ├── app.py             # Arquivo principal da aplicação
│   └── database.py        # Gerenciamento do banco de dados SQLite
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto
```

## Pré-requisitos

Antes de começar, você precisará ter o Python instalado em sua máquina. Recomenda-se usar um ambiente virtual para gerenciar as dependências do projeto.

## Instalação

1. Clone o repositório:
   ```
   git clone <URL_DO_REPOSITORIO>
   cd projeto_inventario
   ```

2. Crie um ambiente virtual:
   ```
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   - No Windows:
     ```
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Uso

1. Execute a aplicação:
   ```
   python src/app.py
   ```

2. Acesse a aplicação no seu navegador em `http://127.0.0.1:5000`.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.