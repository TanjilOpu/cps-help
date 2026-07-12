% 1. Define the Signals
x = [4, 2, 1, 3];                  % Input Signal
y = [4, 10, 13, 13, 10, 7, 3];     % Convolved Output Signal

% 2. Perform Deconvolution
h = deconv(y, x);                 % Recovers the hidden impulse response

% Display the result in the Command Window
disp('Recovered Signal h:');
disp(h);

% 3. Create Time Vectors for Plotting (MATLAB index starts at 0 for time)
time_x = 0:(length(x) - 1);
time_h = 0:(length(h) - 1);
time_y = 0:(length(y) - 1);

% 4. Plot all three signals using discrete stem plots
figure;

% Plot 1: Input Signal
subplot(3, 1, 1);
stem(time_x, x, 'filled', 'b');
title('1. Input Signal x[n]');
xlabel('Time Index (n)');
ylabel('Amplitude');
grid on;

% Plot 2: Recovered Impulse Response
subplot(3, 1, 2);
stem(time_h, h, 'filled', 'g');
title('2. Recovered Impulse Response h[n]');
xlabel('Time Index (n)');
ylabel('Amplitude');
grid on;

% Plot 3: Convolved Output
subplot(3, 1, 3);
stem(time_y, y, 'filled', 'm');
title('3. Convolved Output Signal y[n]');
xlabel('Time Index (n)');
ylabel('Amplitude');
grid on;