## Projeto Banco de Dados I - Análise Exploratória de Dados

O principal objetivo de uma análise exploratória de dados é o de encontrar informações relevantes. Ou seja, dizer se os dados podem retornar valor ou não para determinado segmento.
<br>
<br>
É comum, antes de qualquer análise de dados, estabelecermos perguntas a serem respondidas através dos dados. Como por exemplo: Se temos dados que são referentes a transações de compra, é interessante se perguntar:

- Qual seria o ticket médio destas transações?
- Qual região tem maior número de transações?
- Qual tipo de cartão tem mais transações rejeitadas?

E assim por diante...
<br>
<br>
Entretanto, não existe uma "receita de bolo" a seguir em uma análise de dados. Isso depende muito da experiência de cada envolvido nesse processo.
<br>
<br>
Neste contexto, o seu desafio será o de, a partir da base de dados disponibilizada [aqui](https://github.com/joelsonSantos/banco_de_dados-aula7/tree/main/aula%207), descrever um processo de análise de dados com:

1) 15 perguntas serem respondidas a partir dos dados;

2) Desenvolva scripts de "ingestão" dos dados dos arquivos `produtos.csv` e `vendas.csv`), em tabelas do PostgreSQL com os respectivos nomes: produtos, vendas.
  - **Observação 1**: Crie um banco de dados chamado ecommerce e crie as duas referidas tabelas com seus respectivos dados.
  - **Observação 2**: Os scripts podem ser implementados em python ou puramente em SQL para realizar a ingestão dos dados nas tabelas.

3) Escreva consultas em SQL para responder as perguntas levantadas no item 1.

4) Para cada consulta criada, crie uma **view** no banco de dados para nomeá-la.

5) Utilize as views construídas no item 4, e escreva um Jupyter Notebook para mostrar os insights coletados a partir dos dados.
  - **Observação:** É permitido o uso de gráficos e técnicas estatísticas para apresentar os insights.