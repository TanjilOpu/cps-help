import numpy as np
from scipy import signal

def deconvolve_z_transform(y, x):
    """
    Performs discrete deconvolution using the Z-transform approach.
    Finds h such that Y(z) = X(z) * H(z) -> H(z) = Y(z) / X(z)
    
    Parameters:
    y (list or np.array): The convolved output sequence (Length: M)
    x (list or np.array): The input/filter sequence (Length: N)
    
    Returns:
    list: The deconvolved integer sequence h (Length: M - N + 1)
    """
    len_h = len(y) - len(x) + 1
    
    # In Z-domain, H(z) = Y(z) / X(z). 
    # We treat 'x' as the filter denominator coefficients (a) and 'y' as the input signal.
    # We pad y with zeros to make sure we catch the full length of the response.
    b = np.array(y, dtype=float)
    a = np.array(x, dtype=float)
    
    # signal.lfilter computes the 1D digital filter along the given axis.
    # It solves the difference equation implied by the Z-transform division.
    h_balanced = signal.lfilter(b, a, np.eye(1, len_h)[0])
    
    # Round and convert to integers as requested
    return [int(round(val)) for val in h_balanced]


x = [4, 2, 1, 3]
y = [4, 10, 13, 13, 10, 7, 3]

h_recovered = deconvolve_z_transform(y, x)

print(f"Output Sequence (y): {y}")
print(f"Input Sequence  (x): {x}")
print(f"Deconvolved (h):     {h_recovered}")