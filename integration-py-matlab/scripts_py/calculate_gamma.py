import pandas as pd
from .load_data import load_data

def calculate_gamma(list_of_df,metodo,ativos,start_date,end_date):
    omegaB = list()
    if metodo == "5":
        print("metodo 5")
        list_of_df = list()
        composicao_ibovespa = pd.read_csv("./data/composicao_ibovespa_26_09_22.csv").sort_values('part', ascending=False)[['codigo', 'part']]

        # for ativo in composicao_ibovespa["codigo"]:
        for i in range(0,len(composicao_ibovespa["codigo"])):
            
            df = load_data(composicao_ibovespa[i,1],start_date,end_date)
            if not df.empty:
                omegaB.append(composicao_ibovespa[i,2])
                list_of_df.append(load_data(composicao_ibovespa[i,1],start_date,end_date))

    
    Gamma = list()
    for i in range(1,len(list_of_df)):
        # print(i)
        Gamma.append(list_of_df[i]["variacao"].to_list())

    return Gamma, omegaB