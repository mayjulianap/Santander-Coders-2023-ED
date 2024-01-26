import os

def implementacao_pedente():
    print('Função pendente de implementação.')
    os.system('pause')
    os.system('cls')
    pass


while True:
    os.system('cls')
    print('Seja bem vindo ao sistema financeiro untitled!')
    print('''
        O que você deseja fazer?
          1 - Registrar nova movimentação (receitas e despesas)
          2 - Registrar um novo investimento
          3 - Consultar saldos
          4 - Atualizar registros
          5 - Sair''')
    
    try:
        opcao = int(input())
        if int(opcao) not in range(1, 6):
        # if int(opcao) < 1 or int(opcao) > 5:
            raise ValueError(f'Opção inválida ({(int(opcao))})')
    except ValueError as e:
        print(e)
        os.system('pause')
        os.system('cls')
        continue        
    
    if opcao == 1:
        implementacao_pedente()
        pass

    elif opcao == 2:
        implementacao_pedente()

    elif opcao == 3:
        implementacao_pedente()
    
    elif opcao == 4:
        implementacao_pedente()
    
    elif opcao == 5:
        exit()