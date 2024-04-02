/*
 * View para as questoes: 
 * 1. Qual é o valor médio das vendas?
 * 2. Qual país tem maior número de vendas?
 * 3. Quanto cada país contribuiu para o valor total das vendas?
 * 5. Quais são os 3 produtos menos vendidos?
 */
CREATE VIEW valor_vendas AS 
SELECT p."Codigo", p."Produto", v."Qty", v."ship-country",  REPLACE(p."Preco", '$', '')::NUMERIC  AS ValorVendas
FROM produtos p 
JOIN vendas v ON v."Codigo" = p."Codigo"