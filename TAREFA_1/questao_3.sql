-- Faça uma consulta que selecione o nome e a data de nascimento dos funcionários com idade superior a 21 anos que não são gerentes.
SELECT nome, dtnasc FROM funcionario
WHERE codsupervisor  IS null