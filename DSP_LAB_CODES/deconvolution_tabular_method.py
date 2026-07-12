import matplotlib.pyplot as plt
import numpy as np

def deconvolve_tabular(y, x):
    """
    Performs discrete deconvolution using the tabular (long division) method.
    Finds h such that y = x * h.
    
    Parameters:
    y (list or np.array): The convolved output sequence (Length: M)
    x (list or np.array): The input/filter sequence (Length: N)
    
    Returns:
    list: The deconvolved sequence h (Length: M - N + 1)
    """
    if x[0] == 0:
        raise ValueError("First element of x cannot be zero for the tabular method.")
        
    len_y = len(y)
    len_x = len(x)
    len_h = len_y - len_x + 1
    
    if len_h <= 0:
        raise ValueError("Length of y must be greater than or equal to length of x.")
        
    # Initialize the output sequence h with zeros
    h = [0] * len_h
    
    # Iterative long division process
    for n in range(len_h):
        # Calculate the current sum of previous terms
        current_sum = 0
        for k in range(1, min(n + 1, len_x)):
            current_sum += x[k] * h[n - k]
            
        # Standard long division rule: (y[n] - sum) / x[0]
        h[n] = (y[n] - current_sum) // x[0]
        
    return h



x = [4, 2, 1, 3]
y = [4, 10, 13, 13, 10, 7, 3]

# Perform deconvolution to extract h
h_recovered = deconvolve_tabular(y, x)

print(f"Output Sequence (y): {y}")
print(f"Input Sequence  (x): {x}")
print(f"Deconvolved (h):     {h_recovered}")

# --- Simple Plotting ---
plt.figure(figsize=(8, 10))

# Subplot 1: Input Sequence x
plt.subplot(3, 1, 1)
time_x = np.arange(len(x))
plt.stem(time_x, x)
plt.xlabel('Discrete time')
plt.ylabel('Amplitude')
plt.title('input sequence')
plt.grid();

# Subplot 2: Convolved Output Sequence y
plt.subplot(3, 1, 2)
time_y = np.arange(len(y))
plt.stem(time_y, y)
plt.xlabel('Discrete time')
plt.ylabel('Amplitude')
plt.title('convolution output')
plt.grid(True, linestyle='--', alpha=0.5)

# Subplot 3: Deconvolved Recovered Sequence h
plt.subplot(3, 1, 3)
time_h = np.arange(len(h_recovered))
plt.stem(time_h, h_recovered)
plt.xlabel('Discrete time')
plt.ylabel('Amplitude')
plt.title('deconvolved sequence')
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()