function [y, row, index_dates] = read_index_min_var_erro(file_name)
    T = readtable(file_name);
    row = size(T,1);
    
    index_dates(row,1) = cellstr(''); 
    y = zeros(row,1);
    
    for i = 1:row
        index_dates(i) = T(i,:).data;
        y(i) = T(i,:).variacao;
    end;    
end

