/*
 * 15. Existe uma diferença no volume de vendas entre dias úteis e fins de semana?
 *
 */

   
CREATE VIEW vendas_por_dia_semana AS
SELECT
    CASE 
        WHEN EXTRACT(DOW FROM "Date"::timestamp) IN (0, 6) THEN 'Fim de Semana'
        ELSE 'Dia Útil'
    END AS TipoDeDia,
    COUNT(*) AS TotalDeVendas,
    SUM("Qty") AS QuantidadeTotalVendida
FROM
    vendas
GROUP BY
    TipoDeDia;