function [ omegaB, Gamma ] = calculate_gamma( funds_to_calculate, n_total_fund, row, index_dates, path_to_data, initial_date, final_date , is_min_var )

    omegaB = zeros(n_total_fund,1);
    Gamma = zeros(row, n_total_fund);
    
    for k = 1:n_total_fund
        if is_min_var == 1
            name = funds_to_calculate.codigo(k,1);
        else
            name = funds_to_calculate(k,:);
        end
        
        fund_file_name = strcat(path_to_data, '/', char(name), '_', initial_date, '_', final_date, '.csv');
        
        if exist(fund_file_name, 'file') == 2
            if is_min_var == 1
                omegaB(k,1) = funds_to_calculate.part(k,1)/100;
            end
            [G_fund] = read_fund_data(fund_file_name, index_dates);
            Gamma(:,k) = G_fund;
        else
            fprintf('Não há dados do fundo %s na data especificada.\n', char(name));
        end
    end

end