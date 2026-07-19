% Define the range of n
n = -10:10;

% Generate the unit step sequence
% (n >= 0) returns a logical array of 1s and 0s
u = (n >= 0);

% Plotting the sequence
stem(n, u,'filled','Linewidth',2 );
title('Unit Step Sequence ');
xlabel('n');
ylabel('Amplitude');
grid on;
axis([-11 11 -0.1 1.1]); % Adjust axes for better visibility
yticks([0 1]);