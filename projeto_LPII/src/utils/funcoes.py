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

def read_base_financas(path):
    """
    retorna uma lista de dicionarios, correspondente aos valores de cada linha do arquivo.
    """
    return read_csv(path)


def incluir_manualmente():
    """
    inclui um registro manualmente

    Returns:
        tipo (str): tipo de movimentação
        valor (float): valor da movimentação
        data (str): data da movimentação
    """
    tipo = input("Insira o tipo de registro: Investimento | Despesa | Receita: ")

    valor = float(input("Insira o valor da movimentacao: "))

    data = input("Insira a data da movimentacao (YYYY-MM-DD): ")

    return tipo, valor, data

def incluir_de_csv(path):
    """
    inclui um registro manualmente

    Returns:
        tipo (str): tipo de movimentação
        valor (float): valor da movimentação
        data (str): data da movimentação
    """
    nome_arquivo = input("Insira o nome do arquivo: ")
    
    financas = read_csv(f"{path}/{nome_arquivo}")

    return financas


def incluir_registros_base_dados(**parametros):
    """
    inclui registros na base de dados
    """

    while True:
        print('Como você deseja incluir os registros?')
        print("1. Adicionar manualmente")
        print("2. Importar Base CSV")
        print("0. Sair do programa")
        
        opt = int(input("Digite a opção desejada: "))
        if opt == 0:
            print("Saindo do programa.")
            break
        if opt == 1:
            tipo, valor, data = incluir_manualmente()
            dia = int(data.split("-")[2])
            mes = int(data.split("-")[1])
            ano = int(data.split("-")[0])
            if tipo == "investimento":
                if "taxa" not in parametros:
                    raise ValueError("Tipo de movimentacao investimento requer parametro taxa.")
                else:
                    taxa = parametros["taxa"]
                criar_registro_movimentacao(tipo=tipo, valor=valor,
                                        ano=ano, mes=mes, dia=dia,
                                        taxa=taxa)
            else:
                criar_registro_movimentacao(tipo=tipo, valor=valor,
                                        ano=ano, mes=mes, dia=dia)
        elif opt == 2:
            if "taxa" not in parametros:
                raise ValueError("Tipo de movimentacao investimento requer parametro taxa.")
            else:
                path = parametros["path"]
            financas = incluir_de_csv(path)
            for financa in financas:
                tipo = financa["tipo"]
                valor = float(financa["valor"])
                data = financa["data"]
                dia = int(data.split("-")[2])
                mes = int(data.split("-")[1])
                ano = int(data.split("-")[0])
                if tipo == "investimento":
                    if "taxa" not in parametros:
                        raise ValueError("Tipo de movimentacao investimento requer parametro taxa.")
                    else:
                        taxa = parametros["taxa"]
                    criar_registro_movimentacao(tipo=tipo, valor=valor,
                                            ano=ano, mes=mes, dia=dia,
                                            taxa=taxa)
                else:
                    criar_registro_movimentacao(tipo=tipo, valor=valor,
                                            ano=ano, mes=mes, dia=dia)
        else:
            print("Opção inválida!")


# Verificar qual o último id inserido no registro
def retornar_ultimo_id(tipo: str, path: str):
    """Verifica o último ID registrado no banco de dados.

                Parameters:
                    tipo (str): Tipo de movimentação (receita, despesa ou investimento)

                Returns:
                    ultimo_id (str): Ultimo id registrado no banco de dados escolhido.
            """
    try:
        if tipo.lower() not in ['receita', 'despesa', 'investimento']:
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
            montante = float(ultimo_investimento["montante"]) + capital + float(ultimo_investimento["rendimento"])

            conteudo = [[f'{identificador:07d}', tipo,capital,taxa,ano,mes,dia,round(montante, 2),rendimento]]
            

        with open(f"{database_path}/investimentos.csv", 'a+') as file:

            writer = csv.writer(file, delimiter=',', lineterminator='\n')
            writer.writerows(conteudo)

    else:
        print('Tipo de movimentação inválida.',
              'Escolha entre: "receita", "despesa" ou "investimento"', sep='\n')


def calcular_rendimento(taxa: float=0.003, 
                        valor: float=0, 
                        data_anterior=None, 
                        data_atual=None):
    """
    Cálculo do rendimento de investimento
    M = C * (1 + i)^t
    t = contar_dias_entre_datas(data_anterior,data_atual)

    Parameters:
        taxa (float): taxa de rendimento
        valor (float): valor investido
        data_anterior (datetime): data do investimento anterior
        data_atual (datetime): data atual

    Returns:
        rendimento (float): rendimento do investimento
    """
    
    t = (data_atual - data_anterior).days
    montante_final = valor * (1 + taxa)**t
    rendimento = montante_final- valor
    return round(rendimento, 3)

def deletar_registro(indice: int, tipo: str,
                     database_path: str):

    """
    Determina o tipo de movimentação e deleta o registro correspondente ao indice

    Parameters:
        indice (int): indice do registro a ser deletado
        tipo (str): tipo de movimentação
        database_path (str): caminho do banco de dados
    """
    tipo = tipo.lower()
    if tipo in ['receita', 'despesa']:
        movimentacoes = read_csv(f"{database_path}/movimentacoes.csv")
        registro_retirado = movimentacoes[indice]
        movimentacoes.pop(indice)
        keys = movimentacoes[0].keys()
        with open(f"{database_path}/movimentacoes.csv", 'w') as file:
            dict_writer = csv.DictWriter(file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(movimentacoes)
    elif tipo == 'investimento':
        movimentacoes = read_csv(f"{database_path}/investimentos.csv")
        registro_retirado = movimentacoes[indice]
        movimentacoes.pop(indice)
        keys = movimentacoes[0].keys()
        with open(f"{database_path}/investimentos.csv", 'w') as file:
            dict_writer = csv.DictWriter(file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(movimentacoes)
    else:
        print('Tipo de movimentação inválida.',
              'Escolha entre: "receita", "despesa" ou "investimento"', sep='\n')
    return print(f"Registro {registro_retirado} deletado com sucesso!")



def atualizar_registro(indice: int,
                       tipo: str,
                       database_path: str,
                       data=datetime.datetime.today(),
                       **parametros):
    """
    atualiza o valor ou o tipo de uma movimentação com base na data de registro

    Parameters:
        dia (int): dia da movimentação
        mes (int): mês da movimentação
        ano (int): ano da movimentação
        valor (float): valor da movimentação
        tipo (str): tipo da movimentação
    Returns:
    """
    if tipo in ['receita', 'despesa']:
        movimentacoes = read_csv(f"{database_path}/movimentacoes.csv")
        for nn, mov in enumerate(movimentacoes):
            temp_id = int(mov["id"])
            if temp_id == indice:
                if "valor" in parametros:
                    movimentacoes[temp_id-1]["valor"] = parametros["valor"]
                if "tipo" in parametros:
                    movimentacoes[temp_id-1]["tipo"] = tipo

        keys = movimentacoes[0].keys()
        with open(f"{database_path}/movimentacoes.csv", 'w') as file:
            dict_writer = csv.DictWriter(file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(movimentacoes)
    elif tipo == 'investimento':
        if "taxa" not in parametros:
            raise ValueError("Tipo de movimentacao investimento requer parametro taxa.")
        else:
            taxa = parametros["taxa"]
        investimentos = read_csv(f"{database_path}/investimentos.csv")
        for nn, mov in enumerate(investimentos):
            temp_id = int(mov["id"])
            if temp_id == indice:
                if "valor" in parametros:
                    investimentos[temp_id-1]["capital"] = parametros["valor"]
                if "tipo" in parametros:
                    investimentos[temp_id-1]["tipo"] = tipo
                if "taxa" in parametros:
                    investimentos[temp_id-1]["taxa"] = taxa
                if "capital" in parametros:
                    investimentos[temp_id-1]["capital"] = parametros["capital"]
                break
        
        investimentos_atualizados = []
        for nn, mov in enumerate(investimentos):
            if nn == 0:
                investimentos_atualizados.append({
                    "id": mov["id"],
                    "tipo": mov["tipo"],
                    "capital": mov["capital"],
                    "taxa": mov["taxa"],
                    "ano": mov["ano"],
                    "mes": mov["mes"],
                    "dia": mov["dia"],
                    "montante": mov["montante"],
                    "rendimento": mov["rendimento"]
                })
            else:
                ultimo_investimento = investimentos[nn-1]
                dia_anterior =datetime.datetime(int(ultimo_investimento["ano"]), 
                                                int(ultimo_investimento["mes"]), 
                                                int(ultimo_investimento["dia"]))
                dia_atual = datetime.datetime(int(mov["ano"]), int(mov["mes"]), int(mov["dia"]))

                rendimento = calcular_rendimento(taxa=taxa, 
                                                valor=float(ultimo_investimento["montante"]), 
                                                    data_anterior=dia_anterior, 
                                                    data_atual=dia_atual)
                identificador = nn + 1
                montante = float(ultimo_investimento["montante"]) + float(mov["capital"]) + float(ultimo_investimento["rendimento"])

                investimentos_atualizados.append({
                    "id": mov["id"],
                    "tipo": mov["tipo"],
                    "capital": mov["capital"],
                    "taxa": mov["taxa"],
                    "ano": mov["ano"],
                    "mes": mov["mes"],
                    "dia": mov["dia"],
                    "montante": montante,
                    "rendimento": rendimento
                })

        keys = investimentos_atualizados[0].keys()
        with open(f"{database_path}/investimentos.csv", 'w') as file:
            dict_writer = csv.DictWriter(file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(investimentos_atualizados)
    else:
        print('Tipo de movimentação inválida.',
              'Escolha entre: "receita", "despesa" ou "investimento"', sep='\n')

def agrupar_movimentacoes(movimentacoes, agrupar_por):
    totais = {}
    
    for mov in movimentacoes:
        kss = list(mov.keys())
        chave = None
        data = datetime.datetime(int(mov['ano']), int(mov['mes']), int(mov['dia']))
        if agrupar_por == 'mes':
            chave = f"valor_mes_{data.month}"  # Agrupar pelo mês
        if agrupar_por == 'ano':
            chave = f"valor_ano_{data.year}"  # Agrupar pelo mês
        elif agrupar_por == 'tipo':
            chave = mov['tipo']  # Agrupar pelo tipo de movimentação

        if chave not in totais:
            totais[chave] = 0
        if "valor" in kss:
            totais[chave] += float(mov['valor'])
        else:
            totais[chave] += float(mov['montante'])

    return totais


def exportar_relatorio_json(movimentacoes, formato='json', nome_arquivo='relatorio'):
    if formato == 'json':
        relatorio_json = {}
        for mov in movimentacoes[1:]:
            id_ = mov.pop('id')
            relatorio_json[id_] = mov 
        json_object = json.dumps(relatorio_json, default=str, indent=4)
        with open(f"./database/{nome_arquivo}.json", "w") as outfile:
            outfile.write(json_object)
    # elif formato == 'csv':
    #     relatorio_csv = "ID, Data,Tipo,Valor,Montante\n"
    #     for mov in movimentacoes[1:]:
    #         relatorio_csv += f"{mov['id']},{mov['data']},{mov['tipo']},{mov['valor']},{mov.get('montante_investimento', '')}\n"
    #     return relatorio_csv
    
