def initialization():
    benchmark = input("Escolha o benchmark que deseja rastrear.\n").upper()
    n_ativos = input("Quantos ativos deseja utilizar no rastreamento?\n")
    n_ativos = int(n_ativos)

    print("Digite o código de cada ativo, um por vez.")

    ativos = list()

    for i in range(1, n_ativos + 1):
        ativos.append(input("Ativo {n_ativo}: ".format(n_ativo=i)).upper())

    print("1 - MAD")
    print("2 - Min-Max")
    print("3 - MADD")
    print("4 - DMin-Max")
    print("5 - Mínima Variância do Erro")
    print("6 - Mínimo Erro Não Sistêmico")
    print("7 - Mínimo Erro Quadrático")

    modelo = input("Quais métodos deseja utilizar? (Separados por vírgula)\n")

    start_date = input("Data de treinamento inicial (AAAA-MM-dd): ")
    end_date = input("Data de treinamento final (AAAA-MM-dd): ")

    start_date_val = input("Data de validação inicial (AAAA-MM-dd): ")
    end_date_val = input("Data de validação final (AAAA-MM-dd): ")

    interval = input("Qual o intervalo de tempo de coleta dos dados? (m: mensal, w: semanal, d: diário) ")

    return benchmark, n_ativos, ativos, modelo, start_date, end_date, start_date_val, end_date_val, interval
