/*
 * 14. Quais são os top 5 produtos mais vendidos em cada país?
 *
 */
   
CREATE VIEW produtos_mais_vendidos_por_pais AS
SELECT
    "ship-country" AS Pais,
    "Codigo",
    SUM("Qty") AS TotalVendido,
    RANK() OVER (PARTITION BY "ship-country" ORDER BY SUM("Qty") DESC) AS Ranking
FROM
    vendas
GROUP BY
    "ship-country", "Codigo";