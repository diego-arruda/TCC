function [ w, z_otimo ] = min_err_nao_sist( y, Gamma, n_fund )

    Sigma = cov(Gamma);
    
    betas = zeros(1,n_fund);
    
    stdm = std(y);
    
    for i = 1:n_fund
        covariance = cov(y,Gamma(:,i));
        betas(i) = covariance(1,2)/(stdm^2);
    end;
    
    H = 2*Sigma;
    f = zeros(1,n_fund);
    
    A = -eye(n_fund);
    b = zeros(1,n_fund);
    
    Aeq = [ones(1,n_fund);
           betas];
    beq = [1 1];

    [x, z_otimo] = quadprog(H,f,A,b,Aeq,beq);
    w = x(end-(n_fund-1):end,1);
end

