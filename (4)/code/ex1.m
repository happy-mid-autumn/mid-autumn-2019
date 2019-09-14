%% Initialization
clear ; close all; clc

% parameters setting
mu = 45; sigma = 10;
t_q = 180;  % 正常排队平均时间(min)
p_return = 0.17:0.01:0.25;
t_bound_init = [10; 30]; % t_bound(1)为下界，t_bound(2)为上界
lambda = [0.01; 10000];

% Some gradient descent settings
iterations = 200;
alpha = 0.001;

%% =================== Part 3: Cost and Gradient descent ===================

fprintf('\nTesting the cost function ...\n')

% further testing of the cost function
J = computeCost(mu, sigma, t_q, 0.05, t_bound_init, lambda);
fprintf('With t_bound = [15, 35]\nCost computed = %f\n\n', J);

fprintf('Program paused. Press enter to continue.\n');
pause;

fprintf('\nRunning Gradient Descent ...\n')
% run gradient descent
% for i = 1:20
    [t_bound, J_history] = gradientDescent(mu, sigma, t_q, 0.12, t_bound_init, lambda, alpha, iterations);
    
    fprintf('t_bound found by gradient descent:\n');
    fprintf('%f\n', t_bound);
    syms x;
    int_t_bound = double( int(1/(sqrt(2*pi)*sigma)*exp(-(x - mu)^2/(2*sigma^2)), t_bound(1), t_bound(2)) );
    fprintf('t_s = int(t_bound)*t_q: %f\n', int_t_bound*t_q);

    % % write to file
    % fid = fopen('J-p_return.txt', 'a');
    % fprintf(fid, '%f %f %f %f %f\n', p_return(i), J_history(iterations, 2), J_history(iterations, 3), J_history(iterations, 4), J_history(iterations, 1));
    % fclose(fid);
    % % end of writing file

    fprintf('paused. Press enter to continue.\n');
    pause;
% end


fprintf('Program paused. Press enter to continue.\n');
pause;

% %% ============= Part 4: Visualizing J(t_bound_0, t_bound_1) =============
% fprintf('Visualizing J(t_bound_0, t_bound_1) ...\n')

% % Grid over which we will calculate J
% t_bound0_vals = linspace(0, 30, 31);
% t_bound1_vals = linspace(0, 45, 46);

% % initialize J_vals to a matrix of 0's
% J_vals = zeros(length(t_bound0_vals), length(t_bound1_vals));

% % Fill out J_vals
% for i = 1:length(t_bound0_vals)
%     for j = i:length(t_bound1_vals)
% 	  t = [t_bound0_vals(i); t_bound1_vals(j)];
% 	  J_vals(i,j) = computeCost(mu, sigma, t_q, p_return, t, lambda);
%     end
% end


% % Because of the way meshgrids work in the surf command, we need to
% % transpose J_vals before calling surf, or else the axes will be flipped
% J_vals = J_vals';
% % Surface plot
% figure;
% surf(t_bound0_vals, t_bound1_vals, J_vals)
% xlabel('\t_bound_0'); ylabel('\t_bound_1');

% % Contour plot
% figure;
% % Plot J_vals as 15 contours spaced logarithmically between 0.01 and 100
% contour(t_bound0_vals, t_bound1_vals, J_vals, logspace(-2, 3, 20))
% xlabel('\t_bound_0'); ylabel('\t_bound_1');
% hold on;
% plot(t_bound(1), t_bound(2), 'rx', 'MarkerSize', 10, 'LineWidth', 2);
