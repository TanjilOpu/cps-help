% -------- Analog Signal --------
t = 0:0.001:1;
x = sin(2*pi*5*t);

% -------- Sampling --------
fs = 15;
n = 0:1/fs:1;
xs = sin(2*pi*5*n);

% -------- Quantization --------
L = 8;
xq = round(xs*(L/2))/(L/2);

% -------- Coding --------
codes = round((xq + 1)*(L-1)/2);
binary = dec2bin(codes,3);

% -------- Plot --------
plot(t, x, 'b', 'LineWidth', 1.5);
hold on;

stem(n, xs, 'r', 'filled', 'LineWidth', 1.5);
stem(n, xq, 'k', 'LineWidth', 2);

title('Analog to Digital Conversion');
xlabel('Time');
ylabel('Amplitude');
legend('Analog Signal','Sampled Signal','Quantized Signal');
grid on;

% -------- Display --------
disp('Quantized Values:');
disp(xq);

disp('Binary Codes:');
disp(binary);