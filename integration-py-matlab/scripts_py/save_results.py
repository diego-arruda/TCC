import datetime
import os
import pandas as pd

def save_results(resultado,metodo,dt_start, dt_end, isBenchmark):
    
    metodos = [
        "MAD",
        "MINMAX",
        "MADD",
        "DMINMAX",
        "MIN_VAR_ERR",
        "MIN_ERR_NAO_SIST",
        "MIN_ERR_QUAD"
    ]

    start_month = datetime.datetime.strptime(dt_start, "%Y-%m-%d").strftime("%b").upper()
    start_year = datetime.datetime.strptime(dt_start, "%Y-%m-%d").strftime("%y")

    end_month = datetime.datetime.strptime(dt_end, "%Y-%m-%d").strftime("%b").upper()
    end_year = datetime.datetime.strptime(dt_end, "%Y-%m-%d").strftime("%y")

    if isBenchmark:
        file_name = f"{metodo.upper()}_{start_month}{start_year}_{end_month}{end_year}"
    else:
        file_name = f"{metodos[int(metodo)-1]}_{start_month}{start_year}_{end_month}{end_year}"

    outdir = f"./results/{start_month}{start_year}_{end_month}{end_year}"
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    fullname = os.path.join(outdir, f"{file_name}.csv")    
    resultado.columns = ['variacao']
    # print(resultado)
    print(f"Resultados salvos em: {fullname}\n")
    print("===================================================================\n")
    # print(fullname)
    resultado.to_csv(fullname,index=False)
