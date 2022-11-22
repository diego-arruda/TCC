import os
import pandas as pd


def save_results(res,benchmark, metodo, dt_start_treino, dt_end_treino, dt_start, dt_end, dates, isBenchmark):
    metodos = [
        "MAD",
        "MINMAX",
        "MADD",
        "DMINMAX",
        "MVE",
        "MENS",
        "MEQ"
    ]

    resultado = pd.DataFrame(res)
    resultado.columns = ['variacao_carteira']

    if isBenchmark:
        file_name = f"{metodo.upper()}"
    else:
        file_name = f"{metodos[int(metodo) - 1]}"

    t_dir = f"./results/T_{dt_start_treino}_{dt_end_treino}"
    if not os.path.exists(t_dir):
        os.mkdir(t_dir)
    
    v_dir = f"{t_dir}/V_{dt_start}_{dt_end}"
    if not os.path.exists(v_dir):
        os.mkdir(v_dir)

    fullname = os.path.join(v_dir, f"{file_name}.csv")
    resultado['datas'] = dates
    resultado['variacao_benchmark'] = benchmark.to_list()
    resultado = resultado[['datas', 'variacao_carteira', 'variacao_benchmark']]

    print(f"Resultados salvos em: {fullname}\n")
    print("===================================================================\n")
    resultado.to_csv(fullname, index=False)
