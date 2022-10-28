from scripts_py.load_data import load_data
from scripts_py.initialization import initialization 
from scripts_py.execute_test import execute_test
from scripts_py.save_results import save_results
from scripts_py.calculate_gamma import calculate_gamma
import sys
import matlab.engine

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
    benchmark = load_data(benchmark,start_date,end_date)
    y = benchmark["variacao"].to_list()
    n_periods_len = len(y)
    n_periods = matlab.double(len(y))
    y = matlab.double(y)

    for metodo in metodos:
        Gamma,omegaB = calculate_gamma(metodo,n_periods_len,ativos,start_date,end_date)
        Gamma = matlab.double(Gamma)

        if metodo == '1':
            w, z_otimo, exitflag = eng.mad_method(y, Gamma, n_periods, n_ativos, nargout=3)
        elif metodo == '2':
            w, z_otimo, exitflag = eng.minmax_method(y, Gamma, n_periods, n_ativos, nargout=3)
        elif metodo == '3':
            w, z_otimo, exitflag = eng.madd_method(y, Gamma, n_periods, n_ativos, nargout=3)
        elif metodo == '4':
            w, z_otimo, exitflag = eng.dminmax_method(y, Gamma, n_periods, n_ativos, nargout=3)
        elif metodo == '5':
            n_total_benchmark = len(omegaB)
            omegaB = matlab.double(omegaB)
            w, z_otimo, exitflag = eng.min_var_err(Gamma, n_ativos, n_total_benchmark, omegaB, nargout=3)
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
            print(F"RESULTADOS DO MÉTODO {metodo}\n")
            save_results(resultado,metodo,sim_init_date, sim_final_date,False)

        else: 
            print(f"Não foi possível achar solução para o método {metodo}.\n")

    flag_input = input("Deseja fazer uma nova simulação? (S/N): ")

    if flag_input.upper() != "S":
        eng.quit()
        out_flag = False

