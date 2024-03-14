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
     R: Right Join e Left Join são operações SQL utilizadas para combinar duas ou mais tabelas com base em uma coluna relacionada entre elas.
 - ###  Explique o funcionamento do Full Outer Join e como pode ser feito no MySQL ou MariaDB que não tem mais o comando Full.

