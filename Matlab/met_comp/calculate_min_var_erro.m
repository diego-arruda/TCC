clear all; close all; clc

% Train data
initial_date = 'JAN20';
final_date = 'DEZ20';

comp_ibovespa = readtable('../../python/dados_todos_fundos/composicao_ibovespa_26_09_22.csv');
fund_file_names = blanks(1);

path_to_data = strcat('../../python/dados_todos_fundos/', initial_date, '_', final_date);
index_file_name = strcat(path_to_data, '/', 'ibovespa', '_', initial_date, '_', final_date, '.csv');

[y, row, index_dates] = read_index_min_var_erro(index_file_name);

n_fund = 5;
n_total_fund = length(dir([path_to_data, '\*.csv']));

omegaB = zeros(n_total_fund,1);
Gamma = zeros(row, n_total_fund);

for k = 1:n_total_fund
    fund_file_name = strcat(path_to_data, '/', char(comp_ibovespa.codigo(k,1)), '_', initial_date, '_', final_date, '.csv');
    if exist(fund_file_name, 'file') == 2
        omegaB(k,1) = comp_ibovespa.part(k,1)/100;
        [G_fund] = read_fund_min_var_erro(fund_file_name, index_dates);
        Gamma(:,k) = G_fund;
    else
        comp_ibovespa.codigo(k,1)
    end
end

[ w, z_otimo ] = min_var_err( Gamma, n_fund, n_total_fund, omegaB );

% Test data
% Index
T = readtable(index_file_name);
datas = flip(T.data);
indice = flip(T.variacao);

% GET METHOD RESULT
test_initial_date = 'JAN20';
test_final_date = 'DEZ20';

results = zeros(length(datas),1);

for i = 1:n_fund % pega apenas os 5 primeiro ativos
    fund_file_name = strcat(path_to_data, '/', char(comp_ibovespa.codigo(k,1)), '_', initial_date, '_', final_date, '.csv');
    F = readtable(fund_file_name);
    var = F.variacao;
    results = results + var*w(i);
end;

final_result = flip(results);
format_datas = ['JAN20'; 'FEV20'; 'MAR20'; 'ABR20'; 'MAI20'; 'JUN20'; 'JUL20'; 'AGO20'; 'SET20'; 'OUT20'; 'NOV20'; 'DEZ20'];

figure
plot(final_result, 'o-');
hold on;
plot(indice, 'ko-');
grid on;
set(gca, 'XTick', 1:length(format_datas), 'XTickLabel', format_datas);
legend('Minima Variancia do Erro', 'Ibovespa');