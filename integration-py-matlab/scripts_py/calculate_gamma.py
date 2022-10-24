import pandas as pd
from .load_data import load_data

def calculate_gamma(list_of_df,metodo,ativos,start_date,end_date):

    if metodo == "5":
        print("")
        composicao_ibovespa = pd.read_csv("./data/composicao_ibovespa_26_09_22.csv")

        for ativo in composicao_ibovespa["codigo"]:
            if ativo not in ativos:
                df = load_data(ativo,start_date,end_date)
                if not df.empty:
                    list_of_df.append(load_data(ativo,start_date,end_date))

    Gamma = list()

    for i in range(1,len(list_of_df)):
        # print(i)
        Gamma.append(list_of_df[i]["variacao"].to_list())

    return Gamma