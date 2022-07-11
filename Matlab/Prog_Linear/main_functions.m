clear all; close all; clc

path_to_data = '../../python/dados_historicos_tratados/';

% Train data
initial_date = 'JAN19';
final_date = 'DEZ20';

index_file_name = strcat(path_to_data,'ibovespa_dados_historicos_tratado_', initial_date, '-', final_date, '.csv');
fund_file_names = [
   strcat(path_to_data,'b3sa3_dados_historicos_tratado_', initial_date, '-', final_date, '.csv'),
   strcat(path_to_data,'bbdc4_dados_historicos_tratado_', initial_date, '-', final_date, '.csv'),
   strcat(path_to_data,'itub4_dados_historicos_tratado_', initial_date, '-', final_date, '.csv'),
   strcat(path_to_data,'petr4_dados_historicos_tratado_', initial_date, '-', final_date, '.csv'),
   strcat(path_to_data,'vale3_dados_historicos_tratado_', initial_date, '-', final_date, '.csv'),
    ];

[ w1, z_otimo1 ] = linprog_functions( index_file_name, fund_file_names, 'MAD' );
[ w2, z_otimo2 ] = linprog_functions( index_file_name, fund_file_names, 'MinMax' );
[ w3, z_otimo3 ] = linprog_functions( index_file_name, fund_file_names, 'MADD' );
[ w4, z_otimo4 ] = linprog_functions( index_file_name, fund_file_names, 'DMinMax' );

% Test data
test_initial_date = 'JAN21';
test_final_date = 'DEZ21';

test_index_file_name = strcat(path_to_data,'ibovespa_dados_historicos_tratado_', test_initial_date, '-', test_final_date, '.csv');
test_fund_file_names = [
   strcat(path_to_data,'b3sa3_dados_historicos_tratado_', test_initial_date, '-', test_final_date, '.csv'),
   strcat(path_to_data,'bbdc4_dados_historicos_tratado_', test_initial_date, '-', test_final_date, '.csv'),
   strcat(path_to_data,'itub4_dados_historicos_tratado_', test_initial_date, '-', test_final_date, '.csv'),
   strcat(path_to_data,'petr4_dados_historicos_tratado_', test_initial_date, '-', test_final_date, '.csv'),
   strcat(path_to_data,'vale3_dados_historicos_tratado_', test_initial_date, '-', test_final_date, '.csv'),
    ];

% Index
T = readtable(test_index_file_name);
datas = flip(T.DATA);
indice = flip(T.VARIACAO);

% Funds
row = size(test_fund_file_names,1);

final_result1 = get_method_result( test_fund_file_names, row, datas, w1 );
final_result2 = get_method_result( test_fund_file_names, row, datas, w2 );
final_result3 = get_method_result( test_fund_file_names, row, datas, w3 );
final_result4 = get_method_result( test_fund_file_names, row, datas, w4 );

% Plot
plot(final_result1, 'o-');
hold on;
plot(final_result2, 'o-');
hold on;
plot(final_result3, 'o-');
hold on;
plot(final_result4, 'o-');
hold on;
plot(indice, 'ko-');
grid on;
set(gca, 'XTick', 1:length(datas), 'XTickLabel', datas);
legend('Rastreamento MAD', 'Rastreamento MinMax', 'Rastreamento MADD', 'Rastreamento DMinMax', 'Ibovespa');