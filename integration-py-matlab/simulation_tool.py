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

    benchmark,n_ativos,ativos,metodo,start_date,end_date = initialization()

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

    n_periods = matlab.double(len(y))

    Gamma = np.array(Gamma).T

    y = matlab.double(y)

    Gamma = matlab.double(Gamma)

    print("Iniciando simulação...\n")

    if metodo == '1':
        w, z_otimo = eng.mad_method(y, Gamma, n_periods, n_ativos, nargout=2)
    elif metodo == '2':
        w, z_otimo = eng.minmax_method(y, Gamma, n_periods, n_ativos, nargout=2)
    elif metodo == '3':
        w, z_otimo = eng.madd_method(y, Gamma, n_periods, n_ativos, nargout=2)
    elif metodo == '4':
        w, z_otimo = eng.dminmax_method(y, Gamma, n_periods, n_ativos, nargout=2)
    elif metodo == '5':
        w, z_otimo = eng.min_var_err(Gamma, n_ativos, n_total_benchmark, omegaB, nargout=2) # criar os parametros
    elif metodo == '6':
        w, z_otimo = eng.min_err_nao_sist(y, Gamma, n_ativos, nargout=2)
    elif metodo == '7':
        w, z_otimo = eng.min_err_quad(y, Gamma, n_periods, n_ativos, nargout=2)
    elif metodo == '8':
        w1, z_otimo1 = eng.mad_method(y, Gamma, n_periods, n_ativos, nargout=2)
        w2, z_otimo2 = eng.minmax_method(y, Gamma, n_periods, n_ativos, nargout=2)
        w3, z_otimo3 = eng.madd_method(y, Gamma, n_periods, n_ativos, nargout=2)
        w4, z_otimo4 = eng.dminmax_method(y, Gamma, n_periods, n_ativos, nargout=2)
    elif metodo == '9':
        w5, z_otimo5 = eng.min_var_err(Gamma, n_ativos, n_total_benchmark, omegaB, nargout=2) # criar os parametros
        w6, z_otimo6 = eng.min_err_nao_sist(y, Gamma, n_ativos, nargout=2)
        w7, z_otimo7 = eng.min_err_quad(y, Gamma, n_periods, n_ativos, nargout=2)
    elif metodo == '10':
        w1, z_otimo1 = eng.mad_method(y, Gamma, n_periods, n_ativos, nargout=2)
        w2, z_otimo2 = eng.minmax_method(y, Gamma, n_periods, n_ativos, nargout=2)
        w3, z_otimo3 = eng.madd_method(y, Gamma, n_periods, n_ativos, nargout=2)
        w4, z_otimo4 = eng.dminmax_method(y, Gamma, n_periods, n_ativos, nargout=2)
        w5, z_otimo5 = eng.min_var_err(Gamma, n_ativos, n_total_benchmark, omegaB, nargout=2) # criar os parametros
        w6, z_otimo6 = eng.min_err_nao_sist(y, Gamma, n_ativos, nargout=2)
        w7, z_otimo7 = eng.min_err_quad(y, Gamma, n_periods, n_ativos, nargout=2)
    else:
        sys.exit("Método inválido!")

    print(w)

    flag_input = input("Deseja fazer uma nova simulação? (S/N): ")

    if flag_input.upper() != "S":
        eng.quit()
        out_flag = False

