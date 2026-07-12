import numpy as np
import matplotlib.pyplot as plt

# Input sequence matching the image: x1 = [1 3 0 4]
x1 = np.array([1, 3, 0, 4])

# MATLAB's xcorr(x1, x1) performs full cross-correlation of the signal with itself.
# In NumPy, np.correlate(x1, x1, mode='full') achieves the exact same output.
y = np.correlate(x1, x1, mode='full')

# Create a figure for plotting
plt.figure(figsize=(8, 6))

# --- Subplot 1: Input Sequence ---
plt.subplot(2, 1, 1)
# Create sequential time indices for x1: [0, 1, 2, 3]
time_x1 = np.arange(len(x1)) 
plt.stem(time_x1, x1)
plt.xlabel('Discrete time')
plt.ylabel('Amplitude')
plt.title('input sequence')
plt.grid(True, linestyle='--', alpha=0.5) # Optional: adds a clean look to the stems

# --- Subplot 2: Autocorrelation Sequence ---
plt.subplot(2, 1, 2)
# MATLAB's xcorr shifts center to 0. 
# For a sequence of length N, 'full' correlation generates indices from -(N-1) to +(N-1)
time_y = np.arange(-len(x1) + 1, len(x1)) 
plt.stem(time_y, y)
plt.title('Autocorrelation of the input sequence')
plt.xlabel('Discrete time')
plt.ylabel('Amplitude')
plt.grid(True, linestyle='--', alpha=0.5)

# Adjust layout to prevent text overlapping and display the window
plt.tight_layout()
plt.show()

# --- Print the text output to console ---
print(f"Output Sequence (y): {y.tolist()}")