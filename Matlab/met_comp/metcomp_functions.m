function [ w, z_otimo ] = metcomp_functions( index_file_name, fund_file_names, method )
    [y, row, index_dates] = read_market_index_data(index_file_name);

    n_fund = size(fund_file_names,1);
    Gamma = zeros(row, n_fund);

    for i = 1:n_fund
        fund_file_name = fund_file_names(i,:);
        [G_fund] = read_fund_data(fund_file_name, index_dates);
        Gamma(:,i) = G_fund;
    end;

    if strcmpi('MENS', method)
        fprintf('Metodo %s.\n', method)
        [ w, z_otimo ] = min_err_nao_sist( y, Gamma, n_fund );
%     elseif strcmpi('MinMax', method)
%         fprintf('Metodo %s.\n', method)
%         [ w, z_otimo ] = minmax_method( y, Gamma, row, n_fund );
%     elseif strcmpi('MADD', method)
%         fprintf('Metodo %s.\n', method)
%         [ w, z_otimo ] = madd_method( y, Gamma, row, n_fund );
%     elseif strcmpi('DMinMax', method)
%         fprintf('Metodo %s.\n', method)
%         [ w, z_otimo ] = dminmax_method( y, Gamma, row, n_fund );
    else
        fprintf('Nao ha implementacao do metodo %s. Por favor, escolha outro metodo.\n', method)
    end;

end