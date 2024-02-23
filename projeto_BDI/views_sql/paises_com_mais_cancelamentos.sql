/*
 * 12. Quais paises tiveram mais cancelamentos?
 * 
 */
   
CREATE VIEW paises_com_mais_cancelamentos AS
SELECT
    "ship-country" AS Pais,
    COUNT(*) AS NumeroDeCancelamentos
FROM
    vendas
WHERE
    "Courier Status" = 'Cancelled'
GROUP BY
    "ship-country"
ORDER BY
    NumeroDeCancelamentos DESC;