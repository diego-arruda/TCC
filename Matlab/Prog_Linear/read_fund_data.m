function [ G_fund ] = read_fund_data(fund_file_name, index_dates)
    fund = readtable(fund_file_name);

    row = size(fund,1);
    fund_dates(row,1) = cellstr('');
    G_fund = zeros(row,1);

    for i = 1:row
        fund_dates(i) = fund(i,:).Data;
    end;

    if isequal(index_dates, fund_dates)
        for i = 1:row
            G_fund(i) = fund(i,:).Variacao;
        end;
    else
        fund_name = strsplit(fund_file_name, '_');
        fprintf('As datas do fundo %s não condizem com as datas do índice', char(fund_name(1)))
    end;

end

