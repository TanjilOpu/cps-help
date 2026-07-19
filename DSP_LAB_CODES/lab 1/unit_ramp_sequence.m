% Define the range of n
n = -10:10;

% Generate the unit step sequence
% (n >= 0) returns a logical array of 1s and 0s
u = n.*(n >= 0);

% Plotting the sequence
stem(n, u,'filled','LineWidth',2 );
title('Unit ramp Sequence ');
xlabel('n');
ylabel('Amplitude');
grid on;
axis([-11 11 -1  11]); % Adjust axes for better visibility
yticks(0:11);
