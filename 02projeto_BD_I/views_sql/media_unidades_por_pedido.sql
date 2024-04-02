   
/*
 * 10. Qual é a média de unidades vendidas por pedido?
 */
   
CREATE VIEW media_unidades_por_pedido AS
SELECT
    "Order ID",
    COUNT("Qty"::NUMERIC) AS SomaUnidades
FROM
    vendas
GROUP BY
    "Order ID";