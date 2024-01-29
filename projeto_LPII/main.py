import os
from src.utils.funcoes import *
from prettytable import PrettyTable


PATH = "./database"
TAXA_INVESTIMENTO = 0.01


def implementacao_pedente():
    print('Função pendente de implementação.')
    os.system('pause')
    os.system('cls')
    pass


while True:
    os.system('cls')
    print('Seja bem vindo ao FinAda!\n')
    print('''O que você deseja fazer?
          1 - Incluir novo registro
          2 - Consultar saldos
          3 - Atualizar registros
          0 - Sair''')
    
    try:
        opcao = int(input())
        if int(opcao) not in range(0, 5):
            raise ValueError(f'Opção inválida ({(int(opcao))})')
    except ValueError as e:
        print(e)
        os.system('pause')
        os.system('cls')
        continue        
    
    if opcao == 1:
        os.system('cls')
        incluir_registros_base_dados(taxa=TAXA_INVESTIMENTO, path=PATH)
        # implementacao_pedente()
        # pass

    elif opcao == 2:
        os.system('cls')
        while True:
            print('''Qual saldo deseja consultar?
        1 - Receitas e despesas
        2 - Investimentos
        9. Retornar ao menu principal
        0. Sair do programa''')
            try:
                opcao = int(input())
                if int(opcao) not in range(0, 3) and opcao != 9:
                    raise ValueError(f'Opção inválida ({(int(opcao))})')
            except ValueError as e:
                print(e)
                os.system('pause')
                os.system('cls')
                continue

            if opcao == 0:
                exit()

            elif opcao == 1:
                dados = read_csv(os.path.join(PATH, 'movimentacoes.csv'))
        
                # criação de uma tablea prettytable
                tabela = PrettyTable()
                tabela.field_names = dados[0].keys()
                
                for item in dados:
                    tabela.add_row(item.values())

                print(tabela)

            elif opcao == 2:
                dados = read_csv(os.path.join(PATH, 'investimentos.csv'))
                
                # criação de uma tablea prettytable
                tabela = PrettyTable()
                tabela.field_names = dados[0].keys()
                
                for item in dados:
                    tabela.add_row(item.values())

                print(tabela)
                
            elif opcao == 9:
                break

            os.system('pause')     
            os.system('cls')
            break

    elif opcao == 3:
        implementacao_pedente()
    
    elif opcao == 4:
        implementacao_pedente()
    
    elif opcao == 0:
        exit()