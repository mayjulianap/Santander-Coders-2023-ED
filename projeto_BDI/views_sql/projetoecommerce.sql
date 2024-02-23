SELECT * FROM produtos;

SELECT * FROM vendas;

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



/*
 *View para a questao 
 *4. Qual o dia da semana com mais vendas?
 *
 *Converte o campo Date para datetime com o CAST e usa o DOW (Day of the Week) para
 *extrair o dia da semana (0=Domingo...)
 *
 */

CREATE VIEW mais_vendas_na_semana AS
SELECT EXTRACT(DOW FROM CAST(vendas."Date" AS DATE)) AS DiaDaSemana,
       COUNT(*) AS NumVendas
FROM vendas
GROUP BY DiaDaSemana
ORDER BY NumVendas DESC
;

SELECT * FROM mais_vendas_na_semana;


/*
 * View para a questao
 * 6. Quantas vendas foram realizadas para cada categoria de produto?
 */

CREATE VIEW vendas_por_categoria AS
SELECT v."Style", COUNT(*) AS NumVendas
FROM vendas v
GROUP BY v."Style";

SELECT * FROM vendas_por_categoria;

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