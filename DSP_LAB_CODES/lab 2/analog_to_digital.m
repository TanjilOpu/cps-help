% Analog signal
t = 0:0.001:1;
x = sin(2*pi*5*t);

% Sampling for digital signal
n = 0:0.01:1;
xs = sin(2*pi*5*n);

% Plot
subplot(2,1,1);
plot(t, x, 'LineWidth', 1.5);
title('Analog Signal');
xlabel('Time');
ylabel('Amplitude');
grid on;

subplot(2,1,2);
stem(n, xs, 'filled');
title('Digital Signal (Sampled Signal)');
xlabel('Sample index / Time');
ylabel('Amplitude');
grid on;