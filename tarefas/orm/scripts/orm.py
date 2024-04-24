from sqlalchemy import create_engine, select, update, insert
from sqlalchemy.orm import Session
from sqlalchemy.schema import MetaData, Table

def get_engine():
    # Retorna uma instância do engine conectada ao banco de dados especificado
    return create_engine('postgresql://postgres:postgres@172.18.0.2/atividade_db')

def get_table(engine, table_name):
    # Cria um objeto MetaData associado ao engine fornecido
    metadata = MetaData()
    # Carrega as definições da tabela do banco de dados para o objeto metadata usando reflection
    metadata.reflect(bind=engine)
    # Retorna a tabela especificada a partir do objeto metadata
    return Table(table_name, metadata, autoload_with=engine)
# Inserir uma atividade em algum projeto
def insert_activity(engine, description, project_id, start_date, end_date):
    # Obtém a tabela 'atividade' do banco de dados
    activity_table = get_table(engine, 'atividade')
    # Cria uma instrução de inserção com os valores fornecidos
    stmt = insert(activity_table).values(descricao=description, projeto=project_id, data_inicio=start_date, data_fim=end_date)
    # Abre uma sessão com o banco, executa a instrução e comete a transação
    with Session(engine) as session:
        session.execute(stmt)
        session.commit()
# Atualizar o líder de algum projeto
def update_project(engine, project_code, new_responsible):
    # Obtém a tabela 'projeto' do banco de dados
    project_table = get_table(engine, 'projeto')
    # Cria uma instrução de atualização com base na condição e nos novos valores fornecidos
    stmt = update(project_table).where(project_table.c.codigo == project_code).values(responsavel=new_responsible)
    # Abre uma sessão com o banco, executa a instrução e comete a transação
    with Session(engine) as session:
        session.execute(stmt)
        session.commit()
# Listar todos os projetos e suas atividades
def print_table_contents(engine, table_name):
    # Obtém a tabela especificada do banco de dados
    table = get_table(engine, table_name)
    # Cria uma instrução de seleção para todas as entradas da tabela
    stmt = select(table)
    # Abre uma sessão com o banco, executa a consulta e imprime os resultados
    with Session(engine) as session:
        results = session.execute(stmt)
        for result in results:
            print(result)

if __name__ == "__main__":
    engine = get_engine()
    insert_activity(engine, 'Tarefa de BD', 3, '2024-04-21', '2024-04-22')
    update_project(engine, 1, 3)
    print_table_contents(engine, 'projeto')
    print_table_contents(engine, 'atividade')
