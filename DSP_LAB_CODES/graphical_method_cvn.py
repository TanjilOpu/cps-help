import matplotlib.pyplot as plt

def convolution(x, h):
    m = len(x)
    n = len(h)

    y = [0] * (m + n - 1)

    for i in range(m):
        for j in range(n):
            y[i + j] += x[i] * h[j]

    return y

def graphical_convolution(x, h):

    y = convolution(x, h)

    print("x(k) =", x)
    print("h(k) =", h)
    print("y(n) =", y)

    plt.figure(figsize=(8, 6))

    plt.subplot(3, 1, 1)
    plt.stem(range(len(x)), x)
    plt.title("Input Sequence x(k)")
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.stem(range(len(h)), h)
    plt.title("Impulse Response h(k)")
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.stem(range(len(y)), y)
    plt.title("Convolution Output y(n)")
    plt.grid()

    plt.tight_layout()
    plt.show()

x = [4, 2, 1, 3]
h = [1, 2, 2, 1]

graphical_convolution(x, h)