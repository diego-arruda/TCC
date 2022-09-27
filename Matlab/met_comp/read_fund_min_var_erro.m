function [ G_fund ] = read_fund_min_var_erro(fund_file_name, index_dates)
    fund = readtable(fund_file_name);

    row = size(index_dates,1);
    G_fund = zeros(row,1);

    fund_dates = fund.data;
    
    for i = 1:row
        if ismember(index_dates(i), fund_dates)
            var = fund(ismember(fund.data, index_dates(i)),:).variacao;
            G_fund(i) = var;
        end
    end;

    if not(isequal(index_dates, fund_dates))
        fold_names = strsplit(fund_file_name, '/');
        fund_name = strsplit(fold_names{6}, '_');
        fprintf('As datas do fundo %s nao condizem com as datas do indice\n', char(fund_name{1}))
    end

end



