function [ w, z_otimo, exitflag ] = min_err_quad( y, Gamma, row, n_fund )
    Gamma_T = Gamma';

% Input:
% Gamma_T = matriz com linha - ano, coluna - rentabilidade
% y = vetor com linha - ano, rentabilidade benchmark
% row = n�mero de meses
% n_fund = quantidade de a��es
% z_otimo: valor da fun��o objetivo

    H = 2*Gamma_T'*Gamma_T;
    
   %f = -2*y'*Gamma_T; nosso f anterior
    f = -2*Gamma_T'*y';
 
    I = eye(n_fund); 
    A = [-I];
    b = zeros(n_fund,1);

    Aeq = ones(1,n_fund); %Restri��o e*w = 1 sendo e = Aeq
    
    beq = 1;
   
    [x, z, exitflag] = quadprog(H,f,A,b,Aeq,beq);
    w = x(end-(n_fund-1):end,1);
    z_otimo = z + y'*y;

end

