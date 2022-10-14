function [ w, z_otimo ] = dminmax_method( y, Gamma, row, n_fund )
   var = n_fund+1;
%     rest_ig = 2*row;
%     rest_des = 1;
% 
%     I = eye(row);

    e = ones(n_fund,1);
    et = ones(row,1);

    z1 = zeros(1,n_fund);

    A = [-et -Gamma];
    b = [-y];

    Aeq = [0 e'];
    beq = [1];

    f = [1 z1];

    lb = zeros(var,1);

    [x,z_otimo] = linprog(f,A,b,Aeq,beq,lb);
    w = x(end-(n_fund-1):end,1);

end

