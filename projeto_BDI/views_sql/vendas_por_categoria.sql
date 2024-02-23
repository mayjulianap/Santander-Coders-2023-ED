/*
 * View para a questao
 * 6. Quantas vendas foram realizadas para cada categoria de produto?
 */

CREATE VIEW vendas_por_categoria AS
SELECT v."Style", COUNT(*) AS NumVendas
FROM vendas v
GROUP BY v."Style";

SELECT * FROM vendas_por_categoria;