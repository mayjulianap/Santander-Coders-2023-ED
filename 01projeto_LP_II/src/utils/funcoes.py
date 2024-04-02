import csv
import json
import datetime
from datetime import date
import os
import sys


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

def exportar_csv(lista_dicts, path, tipo):
    keys = lista_dicts[0].keys()
    if tipo in ['receita', 'despesa']:
        filename = "movimentacoes.csv"
    elif tipo == 'investimento':
        filename = "investimentos.csv"
    else:
        raise ValueError("Tipo de movimentacao invalida.")
    with open(f"{path}/{filename}", 'w', newline='') as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(lista_dicts)

def read_base_financas(path):
    """
    retorna uma lista de dicionarios, correspondente aos valores de cada linha do arquivo.
    """
    return read_csv(path)

def incluir_manualmente(parametros:dict):
    """
    inclui um registro manualmente

    Returns:
        tipo (str): tipo de movimentação
        valor (float): valor da movimentação
        data (str): data da movimentação
    """
    # if parametros['tipo'] == "investimento":
    #             try:
    #                 if parametros['tipo'] == "investimento":
    #                     float(parametros['taxa'])
    #                 else:
    #                     taxa = None
                        
    #             except (ValueError, KeyError) as e:
    #                 print(e)
    #                 print('A taxa configurada no código fonte é inválida. Contate o TI.')
    #                 os.system('pause')
    #                 os.system('cls')
    #                 return 400

                # if "taxa" not in parametros:
                #     raise ValueError("Tipo de movimentacao investimento requer parametro taxa.")
                # else:
                # taxa = parametros["taxa"]
                    

    while True:
        os.system('cls')
        try:
            tipo = input("Insira o tipo de registro: Investimento | Despesa | Receita: ")
            
            if tipo.lower() not in ['investimento', 'despesa', 'receita']:
                raise ValueError('Opção inválida!')
            
            elif tipo.lower() == 'investimento':
                float(parametros['taxa'])
                break

            else:
                break

        except KeyError as e:
            print('***A taxa do investimento não está sendo passada como parâmetro. Favor, contatar o TI.\n')
            
            if not 'ipykernel' in sys.modules:
                os.system('pause')

            os.system('cls')
            continue

        except ValueError as e:
            print(e)
            print('***A taxa configurada no código fonte é inválida. Favor, contatar o TI.\n')
            
            if not 'ipykernel' in sys.modules:
                os.system('pause')

            os.system('cls')
            continue

    while True:      
        try:
            valor = float(input("Insira o valor da movimentacao: "))
            
            if valor < 0:
                raise ValueError('O valor deve ser numérico e maior ou igual a 0.')
            else:
                break

        except ValueError as e:
            print(e)
            
            if not 'ipykernel' in sys.modules:
                os.system('pause')

            os.system('cls')
            continue
    
    while True:
        try:
            data = date.fromisoformat(input("Insira a data da movimentacao (YYYY-MM-DD): "))
            break

        except (ValueError, TypeError) as e :
            print(e)
            
            if not 'ipykernel' in sys.modules:
                os.system('pause')

            os.system('cls')
            continue

    return {'tipo':tipo, 'valor':valor, 'data':data}

def incluir_de_csv(path, **parametros):
    """
    inclui um registro manualmente

    Returns:
        tipo (str): tipo de movimentação
        valor (float): valor da movimentação
        data (str): data da movimentação
    """
    if "nome_arquivo" in parametros:
        nome_arquivo = parametros["nome_arquivo"]
    else:
        nome_arquivo = input("Insira o nome do arquivo: ")
    
    financas = read_csv(f"{path}/{nome_arquivo}")

    return financas


def incluir_registros_base_dados(**parametros):
    """
    inclui registros na base de dados
    """
    
        
    while True:
        try:
            if "nome_arquivo" in parametros:
                nome_arquivo = parametros["nome_arquivo"]
                opt = 2
            else:
                print('''Como você deseja incluir os registros?
                    
                    1. Adicionar manualmente
                    2. Importar Base CSV
                    9. Retornar ao menu principal
                    0. Sair do programa
                    ''')
                
                opt = int(input("Digite a opção desejada: "))
                if (opt not in range(0, 3)) and opt != 9:
                    print('entrou no raise')
                    raise ValueError('Opção inválida!')

        except ValueError as e:
            print(f'Opção inválida!')
            
            if not 'ipykernel' in sys.modules:
                os.system('pause')

            os.system('cls')
            continue

        if opt == 0:
            print("Saindo do programa.")
            if not 'ipykernel' in sys.modules:
                exit()
            break

        elif opt == 9:
            break

        elif opt == 1:
            try:
                dict_parametros = incluir_manualmente(parametros)

                if dict_parametros['tipo'].lower() == 'investimento':
                    dict_parametros['taxa'] = parametros['taxa']
                # tipo
                # valor, 
                # data, 
                # taxa
            except TypeError as e:
                print(e)
                continue

            dict_parametros['dia'] = dict_parametros['data'].day
            dict_parametros['mes'] = dict_parametros['data'].month
            dict_parametros['ano'] = dict_parametros['data'].year
            # dia = data.day
            # mes = data.month
            # ano = data.year
        
            # if tipo == "investimento":
            #     try:
            #         float(parametros['taxa'])
            #     except ValueError as e:
            #         print(e)
            #         print('A taxa deve ser um valor decimal (float) com o separador decimal "."')
            #         os.system('pause')
            #         os.system('cls')
            #         continue

            #     if "taxa" not in parametros:
            #         raise ValueError("Tipo de movimentacao investimento requer parametro taxa.")
            #     else:
            #         taxa = parametros["taxa"]

            criar_registro_movimentacao(dict_parametros)
            # criar_registro_movimentacao(tipo=tipo, valor=valor,
        #                             ano=ano, mes=mes, dia=dia,
        #                             taxa=taxa)
        # # else:
        #     criar_registro_movimentacao(tipo=tipo, valor=valor,
        #                             ano=ano, mes=mes, dia=dia)
            
            print('Registro inserido com sucesso.')
            
            if not 'ipykernel' in sys.modules:
                os.system('pause')

            os.system('cls')

            

        elif opt == 2:
            if "path" not in parametros:
                raise ValueError("Ler registros de um CSV requer o diretorio do arquivo.")
            else:
                path = parametros["path"]

            if "nome_arquivo" in parametros:
                nome_arquivo = parametros["nome_arquivo"]
                financas = incluir_de_csv(path, nome_arquivo=nome_arquivo)
            else:
                financas = incluir_de_csv(path)
            # inclui os dados nos bancos de dados
            for financa in financas:
                tipo = financa["tipo"]
                print(tipo)
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

                    registro = {"tipo":tipo, "valor":valor, "dia":dia, "mes":mes, "ano":ano, "taxa":taxa}
                    criar_registro_movimentacao(parametros=registro, database_path=path)
                else:
                    registro = {"tipo":tipo, "valor":valor, "dia":dia, "mes":mes, "ano":ano}
                    criar_registro_movimentacao(parametros=registro, database_path=path)

            
            incluir_rendimento_investimento(database_path=path)

            print('Registros inseridos com sucesso.')

            if not 'ipykernel' in sys.modules:
                os.system('pause')
            os.system('cls')
            
            if "nome_arquivo" in parametros:
                break
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
        with open(os.path.join(path, arquivo), 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            lista_id = [linha[0] for linha in reader if linha[0] != 'id']
            ultimo_id = f'{0:07d}' if len(lista_id) == 0 else max(lista_id)
        return ultimo_id
    except (FileNotFoundError, PermissionError) as e:
        print(f'Erro ao abrir o arquivo {arquivo}: {e}')



# def criar_registro_movimentacao(tipo: str, valor: float,
#                            ano=date.today().year,
#                            mes=date.today().month,
#                            dia=date.today().day,
#                            database_path="database",
#                            **parametros_investimento):
        
def criar_registro_movimentacao(parametros: dict, database_path="database"):
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
    tipo = parametros['tipo'].lower()
    valor = parametros['valor']
    ano = parametros['ano']
    mes = parametros['mes']
    dia = parametros['dia'] 

    # # Validando se o valor é numérico e positivo
    # try:
    #     if valor < 0:
    #         raise ValueError(f'Valor {valor} inválido.')
    # except (TypeError, ValueError) as e:
    #     print(f'Valor {valor} inválido.',
    #           'O valor deve ser numérico e maior ou igual a 0.', sep='\n')

    # Parâmetros validados. Inserindo movimentação de acordo com o tipo.
    if tipo in ['receita', 'despesa']:
        valor = avalia_receita_despesa(tipo, valor)
        identificador = int(retornar_ultimo_id(tipo=tipo, path=database_path)) + 1

        with open(f"{database_path}/movimentacoes.csv", 'a+', newline='') as file:
            identificador = int(retornar_ultimo_id(tipo=tipo, path=database_path)) + 1
            conteudo = [[f'{identificador:07d}', tipo, valor, ano, mes, dia]]
            writer = csv.writer(file, delimiter=',')
            # writer = csv.writer(file, delimiter=',', lineterminator='\n')
            writer.writerows(conteudo)

        print(f"Registro {conteudo} inserido com sucesso no arquivo {database_path}/movimentacoes.csv")

    elif tipo == 'investimento':
        if "taxa" not in parametros:
            raise ValueError("Tipo de movimentacao investimento requer parametro taxa.")
        else:
            taxa = parametros["taxa"]

        identificador = int(retornar_ultimo_id(tipo=tipo, path=database_path)) + 1
        
        # Nesse momento só insere no banco de dados, não calcula o rendimento. 
        # O rendimento é calculad no segundo passo, para todo o banco de dados.
        montante = 0
        rendimento = 0
        conteudo = [[f'{identificador:07d}', tipo, valor, taxa, ano, mes, dia, montante, rendimento]]
        
        with open(f"{database_path}/investimentos.csv", 'a+', newline='') as file:

            writer = csv.writer(file, delimiter=',', lineterminator='\n')
            writer.writerows(conteudo)
        print(f"Registro {conteudo} inserido com sucesso no arquivo {database_path}/investimentos.csv")
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

def incluir_rendimento_investimento(database_path="database"):
    investimentos = read_csv(f"{database_path}/investimentos.csv")
    
    print("Calculando rendimento dos investimentos...")
    for nn, mov in enumerate(investimentos):
        if nn == 0:
            investimentos[nn]["rendimento"] = 0
        else:
            ultimo_investimento = investimentos[nn-1]
            dia_anterior =datetime.datetime(int(ultimo_investimento["ano"]), 
                                            int(ultimo_investimento["mes"]), 
                                            int(ultimo_investimento["dia"]))
            dia_atual = datetime.datetime(int(mov["ano"]), int(mov["mes"]), int(mov["dia"]))

            rendimento = calcular_rendimento(taxa=float(mov["taxa"]), 
                                                valor=float(ultimo_investimento["montante"]), 
                                                data_anterior=dia_anterior, 
                                                data_atual=dia_atual)
            
            montante = float(ultimo_investimento["montante"]) + float(mov["capital"]) + float(ultimo_investimento["rendimento"])

            investimentos[nn]["montante"] = montante
            investimentos[nn]["rendimento"] = rendimento

    exportar_csv(investimentos, database_path, "investimento")
    
    print("Rendimento dos investimentos atualizados com sucesso!")

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
        for nn, mov in enumerate(movimentacoes):
            temp_id = int(mov["id"])
            if temp_id == indice:
                registro_retirado = movimentacoes[nn]
                movimentacoes.pop(nn)
                break
        exportar_csv(movimentacoes, database_path, tipo)

    elif tipo == 'investimento':
        investimentos = read_csv(f"{database_path}/investimentos.csv")
        for nn, mov in enumerate(investimentos):
            temp_id = int(mov["id"])
            if temp_id == indice:
                registro_retirado = investimentos[nn]
                investimentos.pop(nn)
                break
        
        exportar_csv(investimentos, database_path, tipo)
        
    else:
        print('Tipo de movimentação inválida.',
              'Escolha entre: "receita", "despesa" ou "investimento"', sep='\n')
    try:     
        return print(f"Registro {registro_retirado} deletado com sucesso!")
    except UnboundLocalError as e:
        return print(f"Registro {indice} não encontrado.")



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
                    movimentacoes[nn]["valor"] = avalia_receita_despesa(tipo, parametros["valor"])
                if "tipo" in parametros:
                    movimentacoes[nn]["tipo"] = tipo
                print(f"Registro {indice} atualizado para {movimentacoes[nn]} com sucesso!")
                break
        exportar_csv(movimentacoes, database_path, tipo)

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
                    investimentos[nn]["capital"] = parametros["valor"]
                if "tipo" in parametros:
                    investimentos[nn]["tipo"] = tipo
                if "taxa" in parametros:
                    investimentos[nn]["taxa"] = taxa
                if "capital" in parametros:
                    investimentos[nn]["capital"] = parametros["capital"]
                print(f"Registro {indice} atualizado para {investimentos[nn]} com sucesso!")
                break
        
        exportar_csv(investimentos, database_path, tipo)
        incluir_rendimento_investimento(database_path=database_path)
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
        with open(f"./database/{nome_arquivo}.json", "w", newline='') as outfile:
            outfile.write(json_object)
    elif formato == 'csv':
        tipo = movimentacoes[0]["tipo"]
        exportar_csv(movimentacoes, f"./database/", tipo)

    print(f"Relatorio {nome_arquivo} exportado com sucesso!")
    # elif formato == 'csv':
    #     relatorio_csv = "ID, Data,Tipo,Valor,Montante\n"
    #     for mov in movimentacoes[1:]:
    #         relatorio_csv += f"{mov['id']},{mov['data']},{mov['tipo']},{mov['valor']},{mov.get('montante_investimento', '')}\n"
    #     return relatorio_csv
    
