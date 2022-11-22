import pandas as pd
from .load_data import load_data


def calculate_gamma(metodo, n_periods, ativos, start_date, end_date, interval):
    omegaB = list()
    Gamma = list()
    if metodo == "5":
        composicao_ibovespa = (
            pd.read_csv("./data/composicao_ibovespa_26_09_22.csv")
            .sort_values('part', ascending=False)[['codigo', 'part']]
        )

        for i in range(0, len(composicao_ibovespa["codigo"])):
            df = load_data(composicao_ibovespa["codigo"].iloc[i], start_date, end_date, interval)
            if not df.empty:
                variacao = df["variacao"]
                if int(len(variacao)) == int(n_periods):
                    Gamma.append(variacao.to_list())
                    omegaB.append(float(composicao_ibovespa["part"].iloc[i])/100)
                else:
                    mean = variacao.mean()
                    variacao = variacao.to_list()
                    for j in range(0, n_periods - len(variacao)):
                        variacao.insert(0, mean)
                    Gamma.append(variacao)
                    omegaB.append(float(composicao_ibovespa["part"].iloc[i])/100)
    else:
        for ativo in ativos:
            df = load_data(ativo, start_date, end_date, interval)
            Gamma.append(df["variacao"].to_list())

    return Gamma, omegaB
