clear all; close all; clc

index_file_name = 'ibovespa_dados_historicos_tratado.csv';
fund_file_names = [
    'b3sa3_dados_historicos_tratado.csv',
    'bbdc4_dados_historicos_tratado.csv',
    'itub4_dados_historicos_tratado.csv',
    'petr4_dados_historicos_tratado.csv',
    'vale3_dados_historicos_tratado.csv'
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

    
    