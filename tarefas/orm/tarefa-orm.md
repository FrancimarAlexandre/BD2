
# Resumo ODBC na Linguagem python

ODBC (Open Database Connectivity) é um padrão da API que permite a conexão a sistemas de gerenciamento de banco de dados (SGBDs). Isso possibilita que aplicações escritas em diversas linguagens de programação acessem bancos de dados através de uma interface comum. Em Python, isso é particularmente útil, já que permite a interação com uma ampla variedade de bases de dados de maneira eficiente e padronizada.

Para trabalhar com ODBC em python podemos utilizar a biblioteca `pyodbc` que é uma implementação da especificação ODBC para python.

# Resumo ORM Na linguagem python e framework django

__ORM__:Em Python, uma estrutura ORM (Mapeamento Objeto-Relacional) é usada para abstrair as interações do banco de dados, permitindo que os desenvolvedores interajam com um banco de dados usando objetos Python em vez de consultas SQL. Isso torna o código mais fácil de ler, escrever e manter. Abaixo estão algumas das estruturas ORM mais populares disponíveis para Python, juntamente com seus recursos e casos de uso típicos:

## SQLAlchemy

SQLAlchemy é uma das estruturas ORM mais poderosas e flexíveis disponíveis em Python. Ele fornece um conjunto completo de padrões de persistência de nível empresarial bem conhecidos e foi projetado para acesso eficiente e de alto desempenho ao banco de dados.

    Características:
        Padrão de mapeador de dados em que as classes podem ser mapeadas para o banco de dados de várias maneiras abertas.
        Suporta uma ampla variedade de back-ends de banco de dados.
        Linguagem de expressão SQL detalhada.
        Detecção automática de alterações e sincronização de banco de dados usando Unidade de Trabalho.
    Caso de uso típico: é adequado para aplicativos que exigem consultas complexas, modelos de dados e alta flexibilidade na interação com o banco de dados. É amplamente utilizado em aplicações de pequena e grande escala.

# SCRIPTS

<a href="https://github.com/FrancimarAlexandre/BD2/blob/main/tarefas/orm/scripts/odbc.py">ODBC</a>

<a href="https://github.com/FrancimarAlexandre/BD2/blob/main/tarefas/orm/scripts/orm.py">ORM</a>
