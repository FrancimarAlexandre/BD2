
# Resumo ODBC na Linguagem python

ODBC (Open Database Connectivity) é um padrão da API que permite a conexão a sistemas de gerenciamento de banco de dados (SGBDs). Isso possibilita que aplicações escritas em diversas linguagens de programação acessem bancos de dados através de uma interface comum. Em Python, isso é particularmente útil, já que permite a interação com uma ampla variedade de bases de dados de maneira eficiente e padronizada.

Para trabalhar com ODBC em python podemos utilizar a biblioteca `pyodbc` que é uma implementação da especificação ODBC para python.

__instalação__: Primeiro é necessario instalar a biblioteca `pyobdc`
        
        pip install pyobdc

__drives de coneção__:Antes de estabelecer uma coneção, é essencial verificar se o drive ODBC necessario para rodar o SGBD está intalado no sistema.

__Estabelecer uma Conexão__: Para conectar-se ao banco de dados, você precisa criar uma string de conexão, que inclui detalhes como o tipo do driver, o servidor, o banco de dados, o usuário e a senha. Por exemplo:


    import pyodbc
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=nome_servidor;DATABASE=nome_banco;UID=usuario;PWD=senha')


__Executar Consultas__: Com a conexão estabelecida, você pode começar a executar consultas SQL diretamente do Python. Para isso, você cria um cursor a partir do objeto de conexão e utiliza o método execute:

    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM Tabela")
    for row in cursor:
        print(row)

__Inserir, Atualizar e Deletar Dados__: Além de consultar dados, você pode inserir, atualizar e deletar dados usando comandos SQL similares, mas utilizando o método commit da conexão para garantir que as transações sejam salvas:


    cursor.execute("INSERT INTO Tabela (coluna1, coluna2) VALUES (?, ?)", (valor1, valor2))
    cnxn.commit()

__Tratamento de Exceções e Fechamento de Conexão__: É importante tratar exceções para lidar com erros que possam ocorrer durante as operações de banco de dados e também garantir que a conexão com o banco de dados seja fechada adequadamente:

    try:
        cursor.execute("some query")
    except pyodbc.Error as e:
        print("An error occurred:", e)
    finally:
        cnxn.close()



# Resumo ORM Na linguagem python e framework django

__ORM__: (Object-Relational Mapper) é uma técnica usada para mapear tabelas de banco de dados em classes e objetos do Python, facilitando a interação entre o código Python e o banco de dados. Em vez de escrever instruções SQL manualmente, um ORM permite que você interaja com o banco de dados usando objetos e métodos


__Django ORM__: O Django ORM é parte integrante do framework web Django. Ele oferece uma abstração de alto nível sobre um banco de dados relacional, permitindo que você trabalhe com objetos Python em vez de escrever SQL diretamente. É especialmente útil para desenvolvimento rápido de aplicativos web, pois permite que você se concentre no código Python sem alternar para SQL3.

## __Configurando um projeto base com django ORM__
    
__Crie um ambiente virtual__: Usando o módulo interno `venv`
        
        python3 -m venv venv

__ative o ambiente virtual__: Linux

    source venv/bin/activate

__ative o ambiente virtual__: windowns

    venv\scripts\activate

__instale o pacote__: `django django-extensions`, O pacote fornece algumas extensões personalizadas para a estrutura Django.

    pip install django django-extensions

__registre no projeto django__:

    INSTALLED_APPS = [
    # ...
    'django_extensions',
]