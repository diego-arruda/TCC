from .load_data import load_data2
import pandas as pd

# def read_data(benchmark,ativos,start_date,end_date):
#     active_list = list()

#     fullname_benchmark = load_data2(benchmark, start_date, end_date)

#     active_list.append(fullname_benchmark)

#     for ativo in ativos:
#         fullname_ativo = load_data2(ativo, start_date, end_date)
#         active_list.append(fullname_ativo)

#     list_of_df = list()

#     for active in active_list:
#         list_of_df.append(pd.read_csv(active))

#     return list_of_df


def read_data(ativo,start_date,end_date):
    fullname = load_data2(ativo, start_date, end_date)
    df = pd.read_csv(fullname)
    return df