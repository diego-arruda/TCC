function [ w, z_otimo, exitflag ] = mad_method( y, Gamma, row, n_fund )
    Gamma_T = Gamma';
    var = 2*row+n_fund;

    I = eye(row);
    A = [];
    b = [];

    e = ones(n_fund,1);
    et = ones(row,1);

    z = zeros(1,row);
    z1 = zeros(1,n_fund);

    f = [et' et' z1];

    Aeq = [I -I Gamma_T;
           z z e'];
    beq = [y 1];
    lb = zeros(var,1);

    [x, z_otimo, exitflag] = linprog(f,A,b,Aeq,beq,lb);
    w = x(end-(n_fund-1):end,1);

end

