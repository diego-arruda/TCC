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

    benchmark, n_ativos, ativos, metodos, start_date, end_date, sim_init_date, sim_final_date, interval = initialization()
    metodos = list(metodos.split(","))
    benchmark_treino = load_data(benchmark, start_date, end_date, interval)
    y = benchmark_treino["variacao"].to_list()
    n_periods_len = len(y)
    n_periods = matlab.double(len(y))
    y = matlab.double(y)

    for metodo in metodos:
        Gamma, omegaB = calculate_gamma(metodo, n_periods_len, ativos, start_date, end_date, interval)
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

            print("===================================================================\n")
            print(F"RESULTADOS DO MÉTODO {metodo}\n")
            carteira = execute_test(w, ativos, sim_init_date, sim_final_date, interval)
            resultado = carteira.sum(axis=1)
            resultado.columns = ['variacao_carteira']
            benchmark_val = load_data(benchmark, sim_init_date, sim_final_date, interval)
            dates = benchmark_val["data"].to_list()
            save_results(resultado, benchmark_val["variacao"], metodo, start_date, end_date, sim_init_date,
                         sim_final_date, dates, False)

        else:
            print(f"Não foi possível achar solução para o método {metodo}.\n")

    flag_input = input("Deseja fazer uma nova simulação? (S/N): ")

    if flag_input.upper() != "S":
        eng.quit()
        out_flag = False
