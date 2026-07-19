% Define range
n = -5:25;

% Parameters
a = 1.1;          % a > 1 (growing)
w = 0.4*pi;       % frequency
phi = pi/2;          % phase

% Full complex exponential
x = (a.^n) .* exp(1j*(w*n + phi));

% -------- Plot --------
figure;

% Real part
subplot(2,1,1);
stem(n, real(x), 'filled');
hold on;
%plot(n, zeros(size(n)), 'k');
title('Real Part: Re{x(n)}');
xlabel('n');
ylabel('Amplitude');
grid on;

% Imaginary part
subplot(2,1,2);
stem(n, imag(x), 'filled');
hold on;
%plot(n, zeros(size(n)), 'k');
title('Imaginary Part: Im{x(n)}');
xlabel('n');
ylabel('Amplitude');
grid on;