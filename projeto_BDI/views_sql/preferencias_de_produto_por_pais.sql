/*
 * 13. Qual é a relação entre o país de envio e a escolha do produto?
 */
   
CREATE VIEW preferencias_de_produto_por_pais AS
SELECT
    v."ship-country" AS Pais,
    p."Produto",
    COUNT(*) AS QuantidadeVendida
FROM
    vendas v
JOIN
    produtos p ON v."Codigo" = p."Codigo"
GROUP BY
    Pais, p."Produto"
ORDER BY
    Pais, QuantidadeVendida DESC;