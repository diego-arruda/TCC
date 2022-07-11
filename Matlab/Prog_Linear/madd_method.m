function [ w, z_otimo ] = madd_method( y, Gamma, row, n_fund )
    var = 2*row+n_fund;

    I = eye(row);

    e = ones(n_fund,1);
    et = ones(row,1);

    z = zeros(1,row);
    z1 = zeros(1,n_fund);

    A = [-I -Gamma];
    b = [-y];

    Aeq = [z e'];
    beq = [1];

    f = [et' z1];

    lb = zeros(var,1);

    [x,z_otimo] = linprog(f,A,b,Aeq,beq,lb);
    w = x(end-(n_fund-1):end,1);

end

