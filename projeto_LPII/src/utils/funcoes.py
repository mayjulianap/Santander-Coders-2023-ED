import csv
import json
import datetime


def read_csv(path):
    """
    retorna uma lista de listas, onde a primeira lista é o header,
    e as outras correspondem aos valores de cada linha do arquivo.
    """
    with open(path, newline='') as f:
        reader = csv.reader(f)
        linhas = []
        for row in reader:
            linhas.append(row)

    return linhas

def cria_conta_bancaria(data_criacao="01/01/1970"):
   data_datetime = datetime.datetime.strptime(data_criacao, "%d/%m/%Y")
   return [{"data": data_datetime,
           "conta_corrente": 0,
           "investimentos": 0,
           "rendimento": 0,
           "montante_investimento": 0,
           "tipo":"receita",
           "valor": 0,
           "ano": data_datetime.year,
           "mes": data_datetime.month,
           "dia": data_datetime.day}]

def criar_registro_movimentacao(id, data, tipo, valor):
    if tipo == 'despesa':
        valor = -abs(valor)  # Garante que despesa seja armazenada como negativa
    return {"ID": id,
            "data": data,
            "tipo": tipo,
            "valor": valor,
            "ano": data.year,
            "mes": data.month,
            "dia": data.day}


def movimentacao(input_terminal=True, lista_movimentacoes=None):
    movimentacao = []
    if input_terminal:
      entrada = 1
      id = 0
      while entrada !=0:
          data = input("Digite a data da movimentacao (dd/mm/aaa): ")
          tipo = input("Qual o tipo da movimentacao, receita, despesa ou investimento? ")
          valor = abs(float(input("Digite o valor da movimentacao: "))) #garante que o valor seja positivo para qualquer opera nesse momento.
          entrada = int(input("Mais alguma movimentação? Digite 1 para continuar ou 0 para sair. "))
          id += 1
          movimentacao.append(criar_registro_movimentacao(id, datetime.datetime.strptime(data, "%Y-%m-%d"), tipo, valor))
    else:
        moviment = read_csv(lista_movimentacoes)[1:]
        for id, mm in enumerate(moviment):
            # movimentacao.append(criar_registro_movimentacao(datetime.datetime.strptime(mm[0], "%Y-%m-%d"), mm[1], float(mm[2])))
            movimentacao.append(criar_registro_movimentacao(id, datetime.datetime.strptime(mm[0], "%Y-%m-%d"), mm[1], float(mm[2])))

    return movimentacao

def deletar_registro(indice, movimentacoes):
    for i, movimentacao in enumerate(movimentacoes):
        if movimentacao['ID'] == indice:
            del movimentacoes[i]
            break

    return movimentacoes


def calcular_rendimento(taxa=0.003, valor=0, data_anterior=None, data_atual=None):
    # Cálculo do rendimento de investimento
    # M = C * (1 + i)^t
    # t = contar_dias_entre_datas(data_anterior,data_atual)
    t = (data_atual - data_anterior).days
    montante_final = valor * (1 + taxa)**t
    rendimento = montante_final- valor
    return rendimento

def calcular_montante(lista_depositos):
    for i in range(len(lista_depositos)):
        if i == 0:
            rendimento = 0
            montante = lista_depositos[0]["investimentos"]
        else:
            montante_anterior = lista_depositos[i-1]["montante_investimento"]
            investido_agora = lista_depositos[i]["investimentos"]
            rendimento = calcular_rendimento(taxa=0.001,
                                             valor=montante_anterior,
                                             data_anterior=lista_depositos[i-1]["data"],
                                             data_atual=lista_depositos[i]["data"])
            montante = rendimento + investido_agora + montante_anterior

        lista_depositos[i]["rendimento"] = rendimento
        lista_depositos[i]["montante_investimento"] = montante

    return lista_depositos


def extrato_conta(movimentacoes):
    sorted_list = sorted(movimentacoes, key=lambda x: x['data'])
    extrato = cria_conta_bancaria()
    investiment0 = 0
    cc = 0
    for i, mvm in enumerate(sorted_list):
        if mvm['tipo'] in ["receita", "despesa"]:
            cc = mvm["valor"]
            investimento = 0
        else:
            investimento = mvm["valor"]
            cc = 0

        extrato.append({
                          "ID": mvm["ID"],"data": mvm["data"],
                          "conta_corrente": cc,
                          "investimentos": investimento,
                          "rendimento": 0,
                          "montante_investimento": 0,
                          "tipo": mvm['tipo'],
                          "valor": mvm['valor'],
                          "ano": mvm["ano"],
                          "mes": mvm["mes"],
                          "dia": mvm["dia"] 
                        })

    extrato = calcular_montante(extrato)
    return extrato


def atualizar_registro(movimentacoes, indice, valor=None, tipo=None):
    for movimentacao in movimentacoes:
        if movimentacao['ID'] == indice:
            movimentacao.update({"valor": valor, "tipo": tipo})
            break


    
    # if indice < len(movimentacoes):

    #     if valor is not None:
    #         movimentacoes[indice]['valor'] = valor
    #     if tipo is not None:
    #         movimentacoes[indice]['tipo'] = tipo
    return movimentacoes

def exportar_relatorio(movimentacoes, formato='json'):
    if formato == 'json':
        relatorio_json = {}
        for mov in movimentacoes[1:]:
            id_ = mov.pop('ID')
            relatorio_json[id_] = mov 
        return json.dumps(relatorio_json, default=str, indent=4)
    elif formato == 'csv':
        relatorio_csv = "ID, Data,Tipo,Valor,Montante\n"
        for mov in movimentacoes[1:]:
            relatorio_csv += f"{mov['ID']},{mov['data']},{mov['tipo']},{mov['valor']},{mov.get('montante_investimento', '')}\n"
        return relatorio_csv

def agrupar_movimentacoes(movimentacoes, agrupar_por):
    totais = {}

    for mov in movimentacoes:
        chave = None

        if agrupar_por == 'mes':
            chave = f"valor_mes_{mov['data'].month}"  # Agrupar pelo mês
        elif agrupar_por == 'tipo':
            chave = mov['tipo']  # Agrupar pelo tipo de movimentação

        if chave not in totais:
            totais[chave] = 0
        totais[chave] += mov['valor']

    return totais