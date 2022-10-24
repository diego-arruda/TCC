from scripts_py.load_data import load_data
from scripts_py.initialization import initialization 
from scripts_py.execute_test import execute_test
from scripts_py.save_results import save_results
from scripts_py.calculate_gamma import calculate_gamma
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

    benchmark,n_ativos,ativos,metodos,start_date,end_date = initialization()
    metodos = list(metodos.split(","))
    list_of_df = list()
    list_of_df.append(load_data(benchmark,start_date,end_date))

    for ativo in ativos:
        list_of_df.append(load_data(ativo,start_date,end_date))

    y = list_of_df[0]["variacao"].to_list()
    n_periods = matlab.double(len(y))
    # y = np.array(y).T
    y = matlab.double(y)

    print(y)

    for metodo in metodos:
        Gamma = calculate_gamma(list_of_df,metodo,ativos,start_date,end_date)
        # Gamma = np.array(Gamma).T
        Gamma = matlab.double(Gamma)

        # print(Gamma)

        # w = list()
        # exitflag = list()

        if metodo == '1':
            w, z_otimo, exitflag = eng.mad_method(y, Gamma, n_periods, n_ativos, nargout=3)
        elif metodo == '2':
            w, z_otimo, exitflag = eng.minmax_method(y, Gamma, n_periods, n_ativos, nargout=3)
        elif metodo == '3':
            w, z_otimo, exitflag = eng.madd_method(y, Gamma, n_periods, n_ativos, nargout=3)
        elif metodo == '4':
            w, z_otimo, exitflag = eng.dminmax_method(y, Gamma, n_periods, n_ativos, nargout=3)
        elif metodo == '5':
            w, z_otimo, exitflag = eng.min_var_err(Gamma, n_ativos, n_total_benchmark, omegaB, nargout=3) # criar os parametros
        elif metodo == '6':
            w, z_otimo, exitflag = eng.min_err_nao_sist(y, Gamma, n_ativos, nargout=3)
        elif metodo == '7':
            w, z_otimo, exitflag = eng.min_err_quad(y, Gamma, n_periods, n_ativos, nargout=3)
        else:
            sys.exit("Método inválido!")

        if exitflag == 1:
            sim_init_date = input("Início do período de teste desejado (AAAA-MM-dd): ")
            sim_final_date = input("Final do período de teste desejado (AAAA-MM-dd): ")

            carteira = execute_test(w,ativos,sim_init_date, sim_final_date)
            resultado = carteira.sum(axis=1)
            save_results(resultado,metodo,sim_init_date, sim_final_date,False)
            # print(w)

        else: 
            print(f"Não foi possível achar solução para o método {metodo}.\n")

        # if 1 in exitflag:
        #     sim_init_date = input("Início do período de teste desejado (AAAA-MM-dd): ")
        #     sim_final_date = input("Final do período de teste desejado (AAAA-MM-dd): ")

        #     for i in range(len(exitflag)):
        #         if exitflag[i] == 0:
        #             print(f'O método {metodos_executados[i]} falhou.\n')
        #         else:
        #             carteira = execute_test(w[i],ativos,sim_init_date, sim_final_date)
        #             resultado = carteira.sum(axis=1)
        #             save_results(resultado,metodos_executados[i],sim_init_date, sim_final_date,False)
        #             print(resultado)
                    

        #     # results = pd.DataFrame(['carteira','benchmark'])
        #     benchmark_data = load_data(benchmark,sim_init_date,sim_final_date)
        #     save_results(benchmark_data['variacao'],benchmark,sim_init_date,sim_final_date,True)

        #     # print(results)

        # else: 
        #     print("Não foi possível achar solução para o(s) método(s) desejado(s).\n")




    flag_input = input("Deseja fazer uma nova simulação? (S/N): ")

    if flag_input.upper() != "S":
        eng.quit()
        out_flag = False

