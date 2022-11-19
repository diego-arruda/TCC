function [ w, z_otimo ] = min_var_err( Gamma, n_fund, n_total_fund, omegaB )

    Sigma = cov(Gamma);

    H = 2*Sigma;
    f = -2*Sigma*omegaB;

    r = ones(n_total_fund,1);
    e = ones(1, n_total_fund);

    I = eye(n_total_fund); 
    A = -I;
    b = zeros(n_total_fund,1);

    Aeq = [r'; % restrição de que a soma dos pesos de w e wb deve ser igual
           e; % restrição de que a soma dos pesos de w deve ser 1
           zeros(n_total_fund-n_fund,n_fund) eye(n_total_fund-n_fund)]; 
       % restrição para apenas os 5 primeiros pesos de w serem diferentes de 0
    beq = [omegaB'*r;
           1;
           zeros(n_total_fund-n_fund,1)];

    options = optimset('Algorithm','interior-point-convex','Display','final-detailed','MaxIter',500,'TolCon', 0.1);
    [x, z, exitflag,output] = quadprog(H,f,A,b,Aeq,beq,[],[],[],options);
    disp('valor exitflag: ')
    disp(exitflag)
    disp('valor output: ')
    disp(output)
    disp(x)
    w = x(1:n_fund,1);
    z_otimo = z + omegaB'*Sigma*omegaB;
    
end
