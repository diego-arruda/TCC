from .load_data import load_data
import pandas as pd


def execute_test(w,ativos,start_date, end_date):
    carteira = pd.DataFrame()
    for i in range(len(ativos)):
        print(f"Peso encontrado para o ativo {ativos[i]}: {w[i][0]}\n")
        ativo_data = load_data(ativos[i],start_date,end_date)
        ativo_data['variacao'] = w[i][0] * ativo_data['variacao']
        carteira = pd.concat([carteira,ativo_data['variacao']], axis=1)
    return carteira

