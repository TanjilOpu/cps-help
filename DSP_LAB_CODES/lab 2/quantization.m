% Sampled signal
n = 0:0.05:1;
x = sin(2*pi*5*n);

% Quantization levels
L = 8;   % number of levels

% Quantization process
xq = round(x*(L/2))/(L/2);

% Plot
subplot(2,1,1);
stem(n, x, 'filled');
title('Original Sampled Signal');
xlabel('Time');
ylabel('Amplitude');
grid on;

subplot(2,1,2);
stem(n, xq, 'filled');
title('Quantized Signal');
xlabel('Time');
ylabel('Amplitude');
grid on;