
def initialization(): 
    benchmark = input("Escolha o benchmark que deseja rastrear.\n").upper()
    n_ativos = input("Quantos ativos deseja utilizar no rastreamento?\n")
    n_ativos = int(n_ativos)

    print("Digite o código de cada ativo, um por vez.")

    ativos = list()

    for i in range(1,n_ativos+1):
        ativos.append(input("Ativo {n_ativo}: ".format(n_ativo = i)).upper())

    print("1 - MAD")
    print("2 - Min-Max")
    print("3 - MADD")
    print("4 - DMin-Max")
    print("5 - Mínima Variância do Erro")
    print("6 - Mínimo Erro Não Sistêmico")
    print("7 - Mínimo Erro Quadrático")
    print("8 - Métodos de Programação Linear")
    print("9 - Métodos Computacionais")
    print("10 - Todos")

    modelo = input("Qual modelo deseja utilizar?\n")

    start_date = input("Data de treinamento inicial (AAAA-MM-dd): ")
    end_date = input("Data de treinamento final (AAAA-MM-dd): ")

    return benchmark,n_ativos,ativos,modelo, start_date, end_date


    

