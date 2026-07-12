import numpy as np
import matplotlib.pyplot as plt

# 1. Define your input signal
x = [4, 2, 1, 3]

# 2. Create the time/sample index array: [0, 1, 2, 3]
time_x = np.arange(len(x))

# 3. Create the plot window
plt.figure(figsize=(7, 4))

# 4. Use plt.stem to create discrete lines with marker dots
plt.stem(time_x, x, linefmt='b-', markerfmt='bo', basefmt='r-')

# 5. Label your axes properly
plt.xlabel("Time Index (n)")
plt.ylabel("Amplitude")
plt.title("Discrete-Time Signal x[n]")

# 6. Clean up the presentation
plt.xticks(time_x) # Show exact integer numbers on the x-axis
plt.grid(True, linestyle='--', alpha=0.6) # Add subtle background lines

# 7. Display the image
plt.show()