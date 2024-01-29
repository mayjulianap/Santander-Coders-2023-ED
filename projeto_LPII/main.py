import os
from src.utils.funcoes import *


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
        implementacao_pedente()

    elif opcao == 3:
        implementacao_pedente()
    
    elif opcao == 4:
        implementacao_pedente()
    
    elif opcao == 0:
        exit()