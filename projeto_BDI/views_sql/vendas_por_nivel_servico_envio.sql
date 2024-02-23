 /*
 * 9. Como o nível de serviço de envio (ship-service-level) afeta o volume de vendas?
 * 
 */

CREATE VIEW vendas_por_nivel_servico AS
SELECT
    "ship-service-level" AS NivelDeServico,
    COUNT(*) AS NumVendas
FROM
    vendas
GROUP BY
    "ship-service-level"
ORDER BY
    NumVendas DESC;