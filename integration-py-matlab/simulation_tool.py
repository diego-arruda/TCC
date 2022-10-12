from scripts_py.initialization import initialization 
from scripts_py.load_data import load_data
import sys
import matlab.engine
import numpy as np

import pandas as pd

benchmark,n_ativos,ativos,modelo, start_date, end_date = initialization()

# load_flag = load_data(benchmark,ativos,start_date,end_date)

# if load_flag:
#     # print("Não foi possível carregar dados para os ativos/benchmark escolhidos!")
#     sys.exit("Não foi possível carregar dados para os ativos/benchmark escolhidos!")

try:
    eng = matlab.engine.start_matlab()
except:
    sys.exit("Falha na conexão com o Matlab.")

# path_to_data = '../data/'

# omegaB, Gamma = eng.calculate_gamma(ativos, n_ativos, row, index_dates, path_to_data, start_date, end_date , 0, nargout=2)

df = pd.read_csv('./data/JAN22_OUT22/ibovespa_JAN22_OUT22.csv')

df2 = pd.read_csv('./data/JAN22_OUT22/amer3_JAN22_OUT22.csv')

df3 = pd.read_csv('./data/JAN22_OUT22/b3sa3_JAN22_OUT22.csv')

Gamma = [df2["variacao"].to_list(),df3["variacao"].to_list()]

y = df["variacao"].to_list()

y = matlab.double(y)

Gamma = np.array(Gamma).T


Gamma = matlab.double(Gamma)

print(Gamma)

# print(y)


w, z_otimo = eng.min_err_nao_sist(y, Gamma, n_ativos, nargout=2)

print(w)

# teste = eng.teste("teste",nargout=1)

# print(teste)

