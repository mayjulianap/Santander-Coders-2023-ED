/*
 * 11. Quais produtos tiveram mais vendas canceladas?
 * 
 */

   
CREATE VIEW produtos_mais_cancelados AS
SELECT
    v."Codigo",
    p."Produto",
    COUNT(*) AS NumeroDeCancelamentos
FROM
    vendas v
JOIN
    produtos p ON v."Codigo" = p."Codigo"
WHERE
    v."Courier Status" = 'Cancelled' 
GROUP BY
    v."Codigo", p."Produto"
ORDER BY
    NumeroDeCancelamentos DESC;