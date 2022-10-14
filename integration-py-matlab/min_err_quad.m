function [ w, z_otimo ] = min_err_quad( y, Gamma, row, n_fund )

% Input:
% Gamma = matriz com linha - ano, coluna - rentabilidade
% y = vetor com linha - ano, rentabilidade benchmark
% row = número de meses
% n_fund = quantidade de ações
% z_otimo: valor da função objetivo

    H = 2*Gamma'*Gamma;
    
   %f = -2*y'*Gamma; nosso f anterior
    f = -2*Gamma'*y;
 
    I = eye(n_fund); 
    A = [-I];
    b = zeros(n_fund,1);

    Aeq = ones(1,n_fund); %Restrição e*w = 1 sendo e = Aeq
    
    beq = 1;
   
    [x, z] = quadprog(H,f,A,b,Aeq,beq);
    w = x(end-(n_fund-1):end,1);
    z_otimo = z + y'*y;

end

