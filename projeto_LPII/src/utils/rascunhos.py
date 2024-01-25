
# def cria_conta_bancaria(data_criacao="01/01/1970"):
#    data_datetime = datetime.datetime.strptime(data_criacao, "%d/%m/%Y")
#    return [{"data": data_datetime,
#            "conta_corrente": 0,
#            "investimentos": 0,
#            "rendimento": 0,
#            "montante_investimento": 0,
#            "tipo": "receita",
#            "valor": 0,
#            "ano": data_datetime.year,
#            "mes": data_datetime.month,
#            "dia": data_datetime.day}]



# criar funções separadas para consultar e para inserir movimentações

# def movimentacao(input_terminal=True, lista_movimentacoes=None):
#     movimentacao = []
#     if input_terminal:
#       entrada = 1
#       while entrada !=0:
#           data = input("Digite a data da movimentacao (dd/mm/aaa): ")
#           tipo = input("Qual o tipo da movimentacao, receita, despesa ou investimento? ")
#           valor = abs(float(input("Digite o valor da movimentacao: "))) #garante que o valor seja positivo para qualquer opera nesse momento.
#           entrada = int(input("Mais alguma movimentação? Digite 1 para continuar ou 0 para sair. "))
#           movimentacao.append(criar_registro_movimentacao(datetime.datetime.strptime(data, "%Y-%m-%d"), tipo, valor))
#     else:
#         moviment = read_csv(lista_movimentacoes)[1:]
#         for mm in moviment:
#             # movimentacao.append(criar_registro_movimentacao(datetime.datetime.strptime(mm[0], "%Y-%m-%d"), mm[1], float(mm[2])))
#             movimentacao.append(criar_registro_movimentacao(datetime.datetime.strptime(mm[0], "%Y-%m-%d"), mm[1], float(mm[2])))
#
#     return movimentacao


# def calcular_montante(lista_depositos):
#     for i in range(len(lista_depositos)):
#         if i == 0:
#             rendimento = 0
#             montante = lista_depositos[0]["investimentos"]
#         else:
#             montante_anterior = lista_depositos[i-1]["montante_investimento"]
#             investido_agora = lista_depositos[i]["investimentos"]
#             rendimento = calcular_rendimento(taxa=0.001,
#                                              valor=montante_anterior,
#                                              data_anterior=lista_depositos[i-1]["data"],
#                                              data_atual=lista_depositos[i]["data"])
#             montante = rendimento + investido_agora + montante_anterior

#         lista_depositos[i]["rendimento"] = rendimento
#         lista_depositos[i]["montante_investimento"] = montante

#     return lista_depositos



# def extrato_conta(movimentacoes):
#     sorted_list = sorted(movimentacoes, key=lambda x: x['data'])
#     extrato = cria_conta_bancaria()
#     investiment0 = 0
#     cc = 0
#     for i, mvm in enumerate(sorted_list):
#         if mvm['tipo'] in ["receita", "despesa"]:
#             cc = mvm["valor"]
#             investimento = 0
#         else:
#             investimento = mvm["valor"]
#             cc = 0

#         extrato.append({
#                           "ID": mvm["ID"],"data": mvm["data"],
#                           "conta_corrente": cc,
#                           "investimentos": investimento,
#                           "rendimento": 0,
#                           "montante_investimento": 0,
#                           "tipo": mvm['tipo'],
#                           "valor": mvm['valor'],
#                           "ano": mvm["ano"],
#                           "mes": mvm["mes"],
#                           "dia": mvm["dia"] 
#                         })

#     extrato = calcular_montante(extrato)
#     return extrato
