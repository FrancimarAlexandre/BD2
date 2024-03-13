-- Faça uma consulta que selecione o nome de todos os funcionários, exceto o mais idoso.
SELECT nome FROM funcionario
WHERE dtnasc >(SELECT MIN(dtnasc) FROM funcionario);