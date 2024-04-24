import pyodbc

try:
    # Conexão com o banco de dados
    print("conectando ao banco de dados")
    # conn = pyodbc.connect('DRIVER={PostgreSQL ANSI};SERVER=172.18.0.2;DATABASE=atividade_db;UID=postgres;PWD=postgres')
    conn = pyodbc.connect('DRIVER={PostgreSQL Unicode};SERVER=172.18.0.2;DATABASE=atividade_db;UID=postgres;PWD=postgres')

    cursor = conn.cursor()

    # Letra A: Inserir uma atividade em algum projeto
    print("inserindo dados ")
    descricao = 'Nova atividade'
    projeto = 1
    data_inicio = '2024-04-23'
    data_fim = '2024-06-30'
    cursor.execute("INSERT INTO atividade (descricao, projeto, data_inicio, data_fim) VALUES (?, ?, CAST(? AS DATE), CAST(? AS DATE))",
               (descricao, projeto, data_inicio, data_fim))

    conn.commit()  # Salvando a transação

    # Letra B: Atualizar o líder de algum projeto
    novo_lider_id = 2  # Exemplo: Novo líder tem ID 2
    projeto_id = 1  # Exemplo: ID do projeto a ser atualizado
    print("atualizando dados")
    cursor.execute("UPDATE projeto SET responsavel = ? WHERE codigo = ?", (novo_lider_id, projeto_id))
    conn.commit()  # Salvando a transação

    # Letra C: Listar todos os projetos e suas atividades
    print("Listando dados")
    cursor.execute("""
                   SELECT p.codigo, p.nome,
                    a.descricao, 
                    CAST(a.data_inicio AS VARCHAR), 
                    CAST(a.data_fim AS VARCHAR)
                    FROM projeto p
                    LEFT JOIN atividade a ON p.codigo = a.projeto
                   """)
    for row in cursor.fetchall():
        print(row)

except pyodbc.Error as e:
    print("Ocorreu um erro:", e)

finally:
    # Encerrando conexão
    cursor.close()
    conn.close()
