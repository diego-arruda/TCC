function [ final_result ] = get_method_result( test_fund_file_names, row, datas, w )
    results = zeros(length(datas),1);
    
    for i = 1:row
        fund_file_name = test_fund_file_names(i,:);
        F = readtable(fund_file_name);
        var = F.VARIACAO;
        results = results + var*w(i);
    end;

    final_result = flip(results);

end

