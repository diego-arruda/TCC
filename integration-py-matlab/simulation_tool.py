from scripts_py.load_data import load_data2
from scripts_py.initialization import initialization 
from scripts_py.execute_test import execute_test
from scripts_py.read_data import read_data
from scripts_py.save_results import save_results
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
    list_of_df = list()
    list_of_df.append(read_data(benchmark,start_date,end_date))

    for ativo in ativos:
        list_of_df.append(read_data(ativo,start_date,end_date))

    # active_list = list()

    # fullname_benchmark = load_data2(benchmark, start_date, end_date)

    # active_list.append(fullname_benchmark)

    # print("Carregando dados dos ativos...\n")
    # for ativo in ativos:
    #     fullname_ativo = load_data2(ativo, start_date, end_date)
    #     active_list.append(fullname_ativo)

    # list_of_df = list()

    # for active in active_list:
    #     list_of_df.append(pd.read_csv(active))

    Gamma = list()

    for i in range(1,len(list_of_df)):
        print(i)
        Gamma.append(list_of_df[i]["variacao"].to_list())

    y = list_of_df[0]["variacao"].to_list()

    n_periods = matlab.double(len(y))

    Gamma = np.array(Gamma).T

    y = np.array(y).T

    y = matlab.double(y)

    Gamma = matlab.double(Gamma)

    print("Iniciando treinamento...\n")

    simulations = list()

    w = list()
    exitflag = list()

    if metodo == '1':
        w1, z_otimo, exitflag1 = eng.mad_method(y, Gamma, n_periods, n_ativos, nargout=3)
        metodos_executados = [1]
        w = [w1]
        exitflag = [exitflag1]
    elif metodo == '2':
        w2, z_otimo, exitflag2 = eng.minmax_method(y, Gamma, n_periods, n_ativos, nargout=3)
        metodos_executados = [2]
        w = [w2]
        exitflag = [exitflag2]
    elif metodo == '3':
        w3, z_otimo, exitflag3 = eng.madd_method(y, Gamma, n_periods, n_ativos, nargout=3)
        metodos_executados = [3]
        w = [w3]
        exitflag = [exitflag3]
    elif metodo == '4':
        w4, z_otimo, exitflag4 = eng.dminmax_method(y, Gamma, n_periods, n_ativos, nargout=3)
        metodos_executados = [4]
        w = [w4]
        exitflag = [exitflag4]
    elif metodo == '5':
        w5, z_otimo, exitflag5 = eng.min_var_err(Gamma, n_ativos, n_total_benchmark, omegaB, nargout=3) # criar os parametros
        metodos_executados = [5]
        w = [w5]
        exitflag = [exitflag5]
    elif metodo == '6':
        w6, z_otimo, exitflag6 = eng.min_err_nao_sist(y, Gamma, n_ativos, nargout=3)
        metodos_executados = [6]
        w = [w6]
        exitflag = [exitflag6]
    elif metodo == '7':
        w7, z_otimo, exitflag7 = eng.min_err_quad(y, Gamma, n_periods, n_ativos, nargout=3)
        metodos_executados = [7]
        w = [w7]
        exitflag = [exitflag7]
    elif metodo == '8':
        w1, z_otimo1, exitflag1 = eng.mad_method(y, Gamma, n_periods, n_ativos, nargout=3)
        w2, z_otimo2, exitflag2 = eng.minmax_method(y, Gamma, n_periods, n_ativos, nargout=3)
        w3, z_otimo3, exitflag3 = eng.madd_method(y, Gamma, n_periods, n_ativos, nargout=3)
        w4, z_otimo4, exitflag4 = eng.dminmax_method(y, Gamma, n_periods, n_ativos, nargout=3)
        w = [w1,w2,w3,w4]
        z_otimo = [z_otimo1,z_otimo2,z_otimo3,z_otimo4]
        exitflag = [exitflag1,exitflag2,exitflag3,exitflag4]
        metodos_executados = [1,2,3,4]
    elif metodo == '9':
        w5, z_otimo5, exitflag5 = eng.min_var_err(Gamma, n_ativos, n_total_benchmark, omegaB, nargout=3) # criar os parametros
        w6, z_otimo6, exitflag6 = eng.min_err_nao_sist(y, Gamma, n_ativos, nargout=3)
        w7, z_otimo7, exitflag7 = eng.min_err_quad(y, Gamma, n_periods, n_ativos, nargout=3)
        w = [w5,w6,w7]
        z_otimo = [z_otimo5,z_otimo6,z_otimo7]
        exitflag = [exitflag5,exitflag6,exitflag7]
        metodos_executados = [5,6,7]
    elif metodo == '10':
        w1, z_otimo1, exitflag1 = eng.mad_method(y, Gamma, n_periods, n_ativos, nargout=3)
        w2, z_otimo2, exitflag2 = eng.minmax_method(y, Gamma, n_periods, n_ativos, nargout=3)
        w3, z_otimo3, exitflag3 = eng.madd_method(y, Gamma, n_periods, n_ativos, nargout=3)
        w4, z_otimo4, exitflag4 = eng.dminmax_method(y, Gamma, n_periods, n_ativos, nargout=3)
        w5, z_otimo5, exitflag5 = eng.min_var_err(Gamma, n_ativos, n_total_benchmark, omegaB, nargout=3) # criar os parametros
        w6, z_otimo6, exitflag6 = eng.min_err_nao_sist(y, Gamma, n_ativos, nargout=3)
        w7, z_otimo7, exitflag7 = eng.min_err_quad(y, Gamma, n_periods, n_ativos, nargout=3)
        w = [w1,w2,w3,w4,w5,w6,w7]
        z_otimo = [z_otimo1,z_otimo2,z_otimo3,z_otimo4,z_otimo5,z_otimo6,z_otimo7]
        exitflag = [exitflag1,exitflag2,exitflag3,exitflag4,exitflag5,exitflag6,exitflag7]
        metodos_executados = [1,2,3,4,5,6,7]
    else:
        sys.exit("Método inválido!")

    if 1 in exitflag:
        sim_init_date = input("Início do período de teste desejado (AAAA-MM-dd): ")
        sim_final_date = input("Final do período de teste desejado (AAAA-MM-dd): ")

        for i in range(len(exitflag)):
            if exitflag[i] == 0:
                print(f'O método {metodos_executados[i]} falhou.\n')
            else:
                carteira = execute_test(w[i],ativos,sim_init_date, sim_final_date)
                resultado = carteira.sum(axis=1)
                save_results(resultado,metodos_executados[i],sim_init_date, sim_final_date,False)
                print(resultado)
                

        # results = pd.DataFrame(['carteira','benchmark'])
        benchmark_data = read_data(benchmark,sim_init_date,sim_final_date)
        save_results(benchmark_data['variacao'],benchmark,sim_init_date,sim_final_date,True)

        # print(results)

    else: 
        print("Não foi possível achar solução para o(s) método(s) desejado(s).\n")




    flag_input = input("Deseja fazer uma nova simulação? (S/N): ")

    if flag_input.upper() != "S":
        eng.quit()
        out_flag = False

