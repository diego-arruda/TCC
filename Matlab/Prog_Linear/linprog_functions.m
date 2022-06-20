clear all; close all; clc

path_to_data = '../../python/dados_historicos_tratados/';

index_file_name = strcat(path_to_data,'ibovespa_dados_historicos_tratado_JAN20-JAN22.csv');
fund_file_names = [
   strcat(path_to_data,'b3sa3_dados_historicos_tratado_JAN20-JAN22.csv'),
   strcat(path_to_data,'bbdc4_dados_historicos_tratado_JAN20-JAN22.csv'),
   strcat(path_to_data,'itub4_dados_historicos_tratado_JAN20-JAN22.csv'),
   strcat(path_to_data,'petr4_dados_historicos_tratado_JAN20-JAN22.csv'),
   strcat(path_to_data,'vale3_dados_historicos_tratado_JAN20-JAN22.csv')
    ];

[y, row, index_dates] = read_market_index_data(index_file_name);

n_fund = size(fund_file_names,1);
Gamma = zeros(row, n_fund);

for i = 1:n_fund
    fund_file_name = fund_file_names(i,:);
    [G_fund] = read_fund_data(fund_file_name, index_dates);
    Gamma(:,i) = G_fund;
end;

method = 'DMinMax';

if strcmpi('MAD', method)
    fprintf('Método %s.\n', method)
    [ w, z_otimo ] = mad_method( y, Gamma, row, n_fund );
elseif strcmpi('MinMax', method)
    fprintf('Método %s.\n', method)
    [ w, z_otimo ] = minmax_method( y, Gamma, row, n_fund );
elseif strcmpi('MADD', method)
    fprintf('Método %s.\n', method)
    [ w, z_otimo ] = madd_method( y, Gamma, row, n_fund );
elseif strcmpi('DMinMax', method)
    fprintf('Método %s.\n', method)
    [ w, z_otimo ] = dminmax_method( y, Gamma, row, n_fund );
else
    fprintf('Não há a implementação do método %s. Por favor, escolha outro método.\n', method)
end;

    
    