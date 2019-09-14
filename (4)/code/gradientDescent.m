function [t_bound, J_history] = gradientDescent(mu, sigma, t_q, p_return, t_bound, lambda, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn t_bound
%   t_bound = GRADIENTDESCENT(X, y, t_bound, alpha, num_iters) updates t_bound by 
%   taking num_iters gradient steps with learning rate alpha

J_history = zeros(num_iters, 4);
grad = zeros(2, 1);
J_history(1) = computeCost(mu, sigma, t_q, p_return, t_bound, lambda);
iter = 1;
fprintf('iteration %d: t_bound = [%f, %f]\n',iter, t_bound(1), t_bound(2));

for iter = 2:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               t_bound. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %
    
    grad = computeGrad(mu, sigma, t_q, p_return, t_bound, lambda);
    t_bound = t_bound - alpha * grad;
    [J_history(iter, 1), J_history(iter, 2), J_history(iter, 3), J_history(iter, 4)] = computeCost(mu, sigma, t_q, p_return, t_bound, lambda);

    fprintf('J1 = %f\n', J_history(iter, 2));
    fprintf('J2 = %f\n', J_history(iter, 3));
    fprintf('J3 = %f\n', J_history(iter, 4));
    fprintf('J = %f\n', J_history(iter, 1));
    fprintf('iteration %d: t_bound = [%f, %f]\n',iter, t_bound(1), t_bound(2));
end

J_history_x = (1:num_iters)';
figure(1);
plot(J_history_x, J_history(:, 1));
xlabel('iteration time');
ylabel('J_history');

end
