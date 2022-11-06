import datetime
import os
import pandas as pd


def save_results(res,benchmark, metodo, dt_start_treino, dt_end_treino, dt_start, isBenchmark):
    metodos = [
        "MAD",
        "MINMAX",
        "MADD",
        "DMINMAX",
        "MIN_VAR_ERR",
        "MIN_ERR_NAO_SIST",
        "MIN_ERR_QUAD"
    ]

    resultado = pd.DataFrame(res)
    resultado.columns = ['variacao_carteira']

    dates = []
    int_month = int(datetime.datetime.strptime(dt_start, "%Y-%m-%d").strftime("%m"))
    int_year = int(datetime.datetime.strptime(dt_start, "%Y-%m-%d").strftime("%Y"))

    for i in range(len(resultado['variacao_carteira'])):
        date = datetime.date(int_year, int_month, 1)
        dates.append(date.strftime("%b").lower() + (date.strftime("%y")))

        if int_month >= 12:
            int_month = 1
            int_year += 1
        else:
            int_month += 1

    start_date = dates[0].upper()
    end_date = dates[-1].upper()

    if isBenchmark:
        file_name = f"{metodo.upper()}_{start_date}_{end_date}"
    else:
        file_name = f"{metodos[int(metodo) - 1]}_{start_date}_{end_date}"

    # outdir_treino = f"./results/T_{dt_start_treino}_{dt_end_treino}"
    # if not os.path.exists(outdir_treino):
    #     os.mkdir(outdir_treino)

    t_dir = f"./results/T_{dt_start_treino}_{dt_end_treino}"
    if not os.path.exists(t_dir):
        os.mkdir(t_dir)
    
    v_dir = f"{t_dir}/V_{start_date}_{end_date}"
    if not os.path.exists(v_dir):
        os.mkdir(v_dir)

    fullname = os.path.join(v_dir, f"{file_name}.csv")
    resultado['datas'] = dates
    resultado['variacao_benchmark'] = benchmark.to_list()
    resultado = resultado[['datas', 'variacao_carteira', 'variacao_benchmark']]

    print(f"Resultados salvos em: {fullname}\n")
    print("===================================================================\n")
    resultado.to_csv(fullname, index=False)
