# RESPOSTAS DO EXERCÍCIO

# 1)  Faça uma consulta que selecione o nome dos funcionários que recebem salários superiores aos salários pagos no departamento 2.
        SELECT nome FROM funcionario
        WHERE salario > (SELECT  MAX(salario) FROM funcionario
                        WHERE coddepto = (SELECT codgerente FROM departamento
                                            WHERE codigo = 2));
# 2) Faça uma consulta que selecione o nome de todos os funcionários, exceto o mais idoso.
        SELECT nome FROM funcionario
        WHERE dtnasc >(SELECT MIN(dtnasc) FROM funcionario);                                    
# 3) Faça uma consulta que selecione o nome e a data de nascimento dos funcionários com idade superior a 21 anos que não são gerentes.
        SELECT nome, dtnasc FROM funcionario
        WHERE codsupervisor  IS null
# 4) Faça uma consulta que selecione o nome, o salário e o departamento dos funcionários que não são gerentes, ordenando pelo Código do Departamento.
        SELECT nome, salario, coddepto FROM funcionario
        WHERE codsupervisor IS null ORDER BY coddepto 
# 5) Responda as perguntas:
 - ### Explique os problemas de termos valores nulos nos dados.
 - ### Explique o funcionamento do Right e do Left Join.
     R: Right Join e Left Join são tipos operações SQL utilizadas para combinar duas ou mais tabelas com base em uma coluna relacionada entre elas. São essenciais para consultas que necessitam de dados de múltiplas tabelas, permitindo que os usuários vejam como estão relacionados.

     Left -> Usado para recuperar os dados ou registros da tabela a esqueda e dados ou registros correspondentes a tabela a direita.Em alguns casos, se não houver correspondência de dados ou do registro de acordo com a consulta dada pelo programador, a Left Join ainda exibirá ou retornará as linhas da tabela esquerda e mostrará os valores NULL para as colunas da tabela direita

     Right -> usada para recuperar todos os dados ou registros armazenados da tabela mais à direita e os registros correspondentes da tabela mais à esquerda. Em alguns casos, pode haver uma situação em que não há correspondências dos dados, então, nesse caso, o Right Join ainda incluirá as linhas da tabela da direita, mas exibirá os valores NULL para as colunas associadas à tabela da esquerda.
 - ###  Explique o funcionamento do Full Outer Join e como pode ser feito no MySQL ou MariaDB que não tem mais o comando Full.

