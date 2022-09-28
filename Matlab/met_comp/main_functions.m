clear all; close all; clc

path_to_data = '../../python/dados_historicos_tratados/';

% Train data
initial_date = 'JAN20';
final_date = 'DEZ20';

index_file_name = strcat(path_to_data,'ibovespa_dados_historicos_tratado_', initial_date, '-', final_date, '.csv');
fund_file_names = [
   strcat(path_to_data,'b3sa3_dados_historicos_tratado_', initial_date, '-', final_date, '.csv'),
   strcat(path_to_data,'bbdc4_dados_historicos_tratado_', initial_date, '-', final_date, '.csv'),
   strcat(path_to_data,'itub4_dados_historicos_tratado_', initial_date, '-', final_date, '.csv'),
   strcat(path_to_data,'petr4_dados_historicos_tratado_', initial_date, '-', final_date, '.csv'),
   strcat(path_to_data,'vale3_dados_historicos_tratado_', initial_date, '-', final_date, '.csv'),
    ];

[ w1, z_otimo1 ] = metcomp_functions( index_file_name, fund_file_names, 'MENS' );
% Test data
test_initial_date = 'JAN20';
test_final_date = 'DEZ20';

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
% final_result2 = get_method_result( test_fund_file_names, row, datas, w2 );
% final_result3 = get_method_result( test_fund_file_names, row, datas, w3 );
% final_result4 = get_method_result( test_fund_file_names, row, datas, w4 );

% Plot

figure
plot(final_result1, 'o-');
hold on;
% plot(final_result2, 'o-');
% hold on;
% plot(final_result3, 'o-');
% hold on;
% plot(final_result4, 'o-');
% hold on;
plot(indice, 'ko-');
grid on;
set(gca, 'XTick', 1:length(datas), 'XTickLabel', datas);
legend('MENS', 'Ibovespa');
% 
% if isequal(initial_date, test_initial_date) && isequal(final_date, test_final_date)
%     titulo = sprintf('Otimizacao e validacao com dados de %s a %s', initial_date, final_date);
% else
%     titulo = sprintf('Otimizacao com dados de %s a %s e validacao com dados de %s a %s', initial_date, final_date, test_initial_date, test_final_date);
% end;
% 
% title(titulo)
% 
% fname = ('C:\Users\lilea\Documents\TCC\Matlab\met_comp\graficos');
% fig_name = sprintf('%s-%s_%s-%s.png', initial_date, final_date, test_initial_date, test_final_date);
% 
% set(gcf, 'PaperUnits', 'centimeters');
% set(gcf, 'PaperPosition', [0 0 30 15]);
% saveas(gca, fullfile(fname, fig_name));
% 
% final_T = table(datas, indice, final_result1, final_result2, final_result3, final_result4);
% final_T.Properties.VariableNames = [{'Data', 'Ibovespa', 'MAD', 'MinMax', 'MADD', 'DMinMax'}];
% 
% ftable_name = ('C:\Users\lilea\Documents\TCC\Matlab\Prog_Linear\tabelas');
% table_name = sprintf('%s-%s_%s-%s.csv', initial_date, final_date, test_initial_date, test_final_date);
% writetable(final_T,fullfile(ftable_name, table_name));