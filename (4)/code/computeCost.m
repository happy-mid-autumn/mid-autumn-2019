function [J, J1, J2, J3] = computeCost(mu, sigma, t_q, p_return, t_bound, lambda)

J = 0;
syms x;
int_t_bound = double( int(1/(sqrt(2*pi)*sigma)*exp(-(x - mu)^2/(2*sigma^2)), t_bound(1), t_bound(2)) );
J1 = (sum(t_bound)/2 - int_t_bound*t_q)^2;
J2 = lambda(1)*t_bound(2)^2;
J3 = lambda(2)*(int_t_bound - p_return)^2;
J = J1 + J2 + J3;

fprintf('p = int_t_bound: %f\n', int_t_bound);
end
