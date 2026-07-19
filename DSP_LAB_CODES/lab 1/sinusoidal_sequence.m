% Define range
n = -22:25;

% Parameters
A = 1;              % Amplitude
w = 0.1*pi;         % Angular frequency
phi = pi/4;         % Phase shift

% Sinusoidal sequence
x = A * sin(w*n + phi);

% Plot
stem(n, x, 'filled', 'LineWidth', 1.5);
%plot(n,x);
title('Discrete-Time Sinusoidal Signal');
xlabel('n');
ylabel('Amplitude');
grid on;
axis([-23 26 -1.5 1.5]);