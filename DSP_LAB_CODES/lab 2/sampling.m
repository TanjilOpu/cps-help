% Continuous-time (analog) signal
t = 0:0.001:1;
x = sin(2*pi*5*t);

% Sampling
fs = 20;                     % sampling frequency
n = 0:1/fs:1;                % sampling instants
xs = sin(2*pi*5*n);          % sampled signal

% Plot
plot(t, x, 'LineWidth', 1.5);  % analog signal
hold on;
stem(n, xs, 'filled');         % sampled signal

title('Sampling of a Signal');
xlabel('Time');
ylabel('Amplitude');
legend('Analog Signal','Sampled Signal');
grid on;
