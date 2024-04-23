"""
Escolha uma linguagem de programação e crie um programa para acessar o banco de dados AtividadesBD, use algum drive/pacote da linguagem escolhida ODBC/JDBC.
"""
import pyodbc

conn = pyodbc.connect('DRIVER={PostgreSQL ANSI};SERVER=172.18.0.2;DATABASE=atividade_db;UID=postgres;PWD=postgres')

# Criando um cursor
cursor = conn.cursor()

# Encerrando conexão
cursor.close()
conn.close()

    