from scripts_py.initialization import initialization 
from scripts_py.load_data import load_data
import sys

benchmark,n_ativos,ativos,modelo, start_date, end_date = initialization()

load_flag = load_data(benchmark,ativos,start_date,end_date)

if load_flag:
    # print("Não foi possível carregar dados para os ativos/benchmark escolhidos!")
    sys.exit("Não foi possível carregar dados para os ativos/benchmark escolhidos!")
