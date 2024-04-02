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