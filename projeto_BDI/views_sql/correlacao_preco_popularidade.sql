/*
 * 8. Há alguma correlação entre o preço do produto e sua popularidade (quantidade vendida)?
 * 
 */

CREATE VIEW correlacao_preco_popularidade AS
SELECT
    p."Codigo",
    p."Produto",
    REPLACE(p."Preco", '$', '')::NUMERIC AS Preco,
    SUM(v."Qty") AS QuantidadeVendida
FROM
    produtos p
JOIN
    vendas v ON p."Codigo" = v."Codigo"
GROUP BY
    p."Codigo", p."Produto", p."Preco"
ORDER BY
    QuantidadeVendida DESC;