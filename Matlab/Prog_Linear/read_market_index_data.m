function [y, row, index_dates] = read_market_index_data(file_name)
    T = readtable(file_name);
    row = size(T,1);
    
    index_dates(row,1) = cellstr(''); 
    y = zeros(row,1);
    
    for i = 1:row
        index_dates(i) = T(i,:).DATA;
        y(i) = T(i,:).VARIACAO;
    end;
    
end
