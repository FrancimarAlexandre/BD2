-- Faça uma consulta que selecione o nome dos funcionários que recebem salários superiores aos salários pagos no departamento 2.

SELECT nome FROM funcionario
WHERE salario > (SELECT  MAX(salario) FROM funcionario
				  WHERE coddepto = (SELECT codgerente FROM departamento
									WHERE codigo = 2));