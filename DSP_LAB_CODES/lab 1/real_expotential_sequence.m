% Define range
n = -10:10;

% Parameters
A = 1;
a = 0.8;   % try >1 or <1

% Real exponential sequence
x = (a.^n);

% Plot
stem(n, x, 'filled');
title('Real Exponential Sequence');
xlabel('n');
ylabel('Amplitude');
grid on;