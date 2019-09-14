function grad = computeGrad(mu, sigma, t_q, p_return, t_bound, lambda)

grad = zeros(2, 1);

syms x;
int_t_bound = double( int(1/(sqrt(2*pi)*sigma)*exp(-(x - mu)^2/(2*sigma^2)), t_bound(1), t_bound(2)) );
f_bound = zeros(2, 1);
f_bound(1) = 1/(sqrt(2*pi)*sigma) * exp(-(t_bound(1) - mu)^2/(2*sigma^2));
f_bound(2) = 1/(sqrt(2*pi)*sigma) * exp(-(t_bound(2) - mu)^2/(2*sigma^2));
grad(1) = 2*(sum(t_bound)/2 - int_t_bound*t_q)*(1/2 + f_bound(1)*t_q) + lambda(2)*2*(int_t_bound - p_return)*(-f_bound(1));
grad(2) = 2*(sum(t_bound)/2 - int_t_bound*t_q)*(1/2 - f_bound(2)*t_q) + lambda(1)*2*t_bound(2) + lambda(2)*2*(int_t_bound - p_return)*(f_bound(2));