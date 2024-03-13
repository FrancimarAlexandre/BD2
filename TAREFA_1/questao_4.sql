-- Faça uma consulta que selecione o nome, o salário e o departamento dos funcionários que não são gerentes, ordenando pelo Código do Departamento.

SELECT nome, salario, coddepto FROM funcionario
WHERE codsupervisor IS null ORDER BY coddepto 