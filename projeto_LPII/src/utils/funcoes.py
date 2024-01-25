import csv
import json
import datetime
from datetime import date

def avalia_receita_despesa(tipo: str, valor: float):
    if tipo == 'despesa':
        valor = -abs(valor)
        return valor
    else:
        return valor

def read_csv(path):
    """
    retorna uma lista de dicionarios, correspondente aos valores de cada linha do arquivo.
    """
    lista_de_dicionarios = []
    with open(path, newline='') as f:
        leitor_csv = csv.DictReader(f)
        for linha in leitor_csv:
            lista_de_dicionarios.append(linha)
    return lista_de_dicionarios


# Verificar qual o último id inserido no registro
def retornar_ultimo_id(tipo: str, path: str):
    """Verifica o último ID registrado no banco de dados.

                Parameters:
                    tipo (str): Tipo de movimentação (receita, despesa ou investimento)

                Returns:
                    ultimo_id (str): Ultimo id registrado no banco de dados escolhido.
            """
    try:
        if tipo.lower() not in ['receita', 'investimento']:
            raise ValueError("Tipo de movimentação inválido.") # criar classe de erro
    except (ValueError, AttributeError) as e:
        return tipo, e

    arquivo = "investimentos.csv" if tipo.lower() == 'investimento' else "movimentacoes.csv"

    try:
        with open(f"{path}/{arquivo}", 'r') as file:
            reader = csv.reader(file, delimiter=',', lineterminator='\n', )
            lista_id = [linha[0] for linha in reader if linha[0] != 'id']
            ultimo_id = f'{0:07d}' if len(lista_id) == 0 else max(lista_id)
        return ultimo_id
    except (FileNotFoundError, PermissionError) as e:
        print(f'Erro ao abrir o arquivo {arquivo}: {e}')



def criar_registro_movimentacao(tipo: str, valor: float,
                           ano=date.today().year,
                           mes=date.today().month,
                           dia=date.today().day,
                           database_path="database",
                           **parametros_investimento):
    """Registra uma movimentação financeira.

            Parameters:
                tipo (str): Tipo de movimentação (receita, despesa ou investimento)
                valor (float): Valor da movimentação
                ano (int): ano da movimentação
                mes (int): dia da movimentação
                dia (int): dia da movimentação

            Keyword Args:
                capital (str): capital investido (float),
                taxa (str): taxa do investimento (float)

            Returns:
                None
        """
    tipo = tipo.lower()

    
        
    # Validando os parâmetros de entrada
    try:
        dia, mes, ano = map(int, [dia, mes, ano])
        data = date(ano, mes, dia)
    # Tratamento de erro para digitação de valores não numéricos para dia, mes ou ano
    except ValueError as e:
        print(e, 'Erro ao registrar a data.',
              'Dia, mês ou ano inválido(s).', sep='\n')

    # Validando se o valor é numérico e positivo
    try:
        if valor < 0:
            raise ValueError(f'Valor {valor} inválido.')
    except (TypeError, ValueError) as e:
        print(f'Valor {valor} inválido.',
              'O valor deve ser numérico e maior ou igual a 0.', sep='\n')

    # Parâmetros validados. Inserindo movimentação de acordo com o tipo.
    if tipo in ['receita', 'despesa']:
        valor = avalia_receita_despesa(tipo, valor)
        identificador = int(retornar_ultimo_id(tipo=tipo, path=database_path)) + 1
        with open(f"{database_path}/movimentacoes.csv", 'a+') as file:
            identificador = int(retornar_ultimo_id(tipo=tipo, path=database_path)) + 1
            conteudo = [[f'{identificador:07d}', tipo, valor, ano, mes, dia]]
            print(conteudo)
            writer = csv.writer(file, delimiter=',', lineterminator='\n')
            writer.writerows(conteudo)

    elif tipo == 'investimento':
        if "taxa" not in parametros_investimento:
            raise ValueError("Tipo de movimentacao investimento requer parametro taxa.")
        else:
            taxa = parametros_investimento["taxa"]

        ultimo_registro_investimentos = int(retornar_ultimo_id(tipo=tipo, path=database_path))
        if ultimo_registro_investimentos ==0:
            identificador = ultimo_registro_investimentos + 1
            rendimento = 0
            capital = valor
            montante=capital
            conteudo = [[f'{identificador:07d}', tipo, capital, taxa, ano, mes, dia, montante, rendimento]]
        else:
            ultimo_investimento = read_csv(f"{database_path}/investimentos.csv")[-1]
            dia_anterior =datetime.datetime(int(ultimo_investimento["ano"]), 
                                            int(ultimo_investimento["mes"]), 
                                            int(ultimo_investimento["dia"]))
            dia_atual = datetime.datetime(ano, mes, dia)

            rendimento = calcular_rendimento(taxa=taxa, 
                                              valor=float(ultimo_investimento["montante"]), 
                                                data_anterior=dia_anterior, 
                                                data_atual=dia_atual)
            identificador = ultimo_registro_investimentos + 1
            capital = valor
            montante = float(ultimo_investimento["montante"]) + capital + rendimento

            conteudo = [[f'{identificador:07d}', tipo,capital,taxa,ano,mes,dia,montante,rendimento]]
            

        with open(f"{database_path}/investimentos.csv", 'a+') as file:

            writer = csv.writer(file, delimiter=',', lineterminator='\n')
            writer.writerows(conteudo)

    else:
        print('Tipo de movimentação inválida.',
              'Escolha entre: "receita", "despesa" ou "investimento"', sep='\n')
    #     return

    # return

def deletar_registro(indice, movimentacoes):
    for i, movimentacao in enumerate(movimentacoes):
        if movimentacao['ID'] == indice:
            del movimentacoes[i]
            break

    return movimentacoes


def calcular_rendimento(taxa: float=0.003, 
                        valor: float=0, 
                        data_anterior=None, 
                        data_atual=None):
    # Cálculo do rendimento de investimento
    # M = C * (1 + i)^t
    # t = contar_dias_entre_datas(data_anterior,data_atual)
    t = (data_atual - data_anterior).days
    montante_final = valor * (1 + taxa)**t
    rendimento = montante_final- valor
    return round(rendimento, 3)


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