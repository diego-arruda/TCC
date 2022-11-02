import datetime
import os
import pandas as pd


def save_results(res, metodo, dt_start, isBenchmark):
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
    resultado.columns = ['variacao']

    dates = []
    int_month = int(datetime.datetime.strptime(dt_start, "%Y-%m-%d").strftime("%m"))
    int_year = int(datetime.datetime.strptime(dt_start, "%Y-%m-%d").strftime("%Y"))

    for i in range(len(resultado['variacao'])):
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

    outdir = f"./results/{start_date}_{end_date}"
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    fullname = os.path.join(outdir, f"{file_name}.csv")
    resultado['datas'] = dates
    resultado = resultado[['datas', 'variacao']]

    print(f"Resultados salvos em: {fullname}\n")
    print("===================================================================\n")
    resultado.to_csv(fullname, index=False)
