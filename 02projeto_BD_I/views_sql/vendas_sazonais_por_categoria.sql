/*
 * 
 * 7. Existe alguma tendência sazonal nas vendas de determinadas categorias de produtos?
 */

CREATE VIEW vendas_sazonais_por_categoria AS
SELECT
    EXTRACT(YEAR FROM CAST(vendas."Date" AS DATE)) AS Ano,
    EXTRACT(MONTH FROM CAST(vendas."Date" AS DATE)) AS Mes,
    vendas."Style",
    COUNT(*) AS NumVendas
FROM vendas
GROUP BY Ano, Mes, vendas."Style"
ORDER BY Ano, Mes, vendas."Style";

SELECT * FROM vendas_sazonais_por_categoria;