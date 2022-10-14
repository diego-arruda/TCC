from scripts_py.load_data import load_data2
from scripts_py.initialization import initialization 
# from scripts_py.load_data import load_data
import sys
import matlab.engine
import numpy as np

import pandas as pd


print("Estabelecendo conexão com o Matlab...\n")
try:
    eng = matlab.engine.start_matlab()
except:
    sys.exit("Falha na conexão com o Matlab.")

print("Conexão estabelecida!\n")

out_flag = True

while out_flag:

    benchmark,n_ativos,ativos,modelo, start_date, end_date = initialization()

    active_list = list()

    fullname_benchmark = load_data2(benchmark, start_date, end_date)

    active_list.append(fullname_benchmark)

    print("Carregando dados dos ativos...\n")
    for ativo in ativos:
        fullname_ativo = load_data2(ativo, start_date, end_date)
        active_list.append(fullname_ativo)

    list_of_df = list()

    for active in active_list:
        list_of_df.append(pd.read_csv(active))

    Gamma = list()

    for i in range(1,len(list_of_df)):
        print(i)
        Gamma.append(list_of_df[i]["variacao"].to_list())

    y = list_of_df[0]["variacao"].to_list()

    Gamma = np.array(Gamma).T

    y = matlab.double(y)

    Gamma = matlab.double(Gamma)

    print("Iniciando simulação...\n")

    w, z_otimo = eng.min_err_nao_sist(y, Gamma, n_ativos, nargout=2)

    print(w)

    flag_input = input("Deseja fazer uma nova simulação? (S/N): ")

    if flag_input.upper() != "S":
        eng.quit()
        out_flag = False

