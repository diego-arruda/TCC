function [ w, z_otimo, exitflag ] = min_var_err( Gamma, n_fund, n_total_fund, omegaB )
    Gamma_T = Gamma';
    omegaB = omegaB';
    Sigma = cov(Gamma_T);

    H = 2*Sigma;
    f = -2*Sigma*omegaB;

    r = ones(n_total_fund,1);
    e = ones(1, n_total_fund);

    I = eye(n_total_fund); 
    A = -I;
    b = zeros(n_total_fund,1);

    Aeq = [r'; % restri��o de que a soma dos pesos de w e wb deve ser igual
           e; % restri��o de que a soma dos pesos de w deve ser 1
           zeros(n_total_fund-n_fund,n_fund) eye(n_total_fund-n_fund)]; 
       % restri��o para apenas os 5 primeiros pesos de w serem diferentes de 0
    beq = [omegaB'*r;
           1;
           zeros(n_total_fund-n_fund,1)];

    options = optimset('Display', 'off','LargeScale', 'off','MaxIter',1000);
    [x, z, exitflag] = quadprog(H,f,A,b,Aeq,beq,[],[],[],options);
    w = x(1:n_fund,1);
    z_otimo = z + omegaB'*Sigma*omegaB;
    
end
