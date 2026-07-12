def convolution(x, h):
    m = len(x)
    n = len(h)

    y = [0]*(m+n-1)

    for i in range(m):
        for j in range(n):
            y[i+j] += x[i]*h[j]

    return y


def tabular_array_method(x, h):

    print("\nTabular Array Method\n")

    for i in range(len(x)):

        row = "    "*i

        for j in range(len(h)):
            row += str(x[i]*h[j]).rjust(4) #rjust to align the numbers in the output (rjust is right justify)

        print(row)

    print("\nConvolution Output:")
    print(convolution(x,h))


x = [4, 2, 1, 3]
h = [1, 2, 2, 1]

tabular_array_method(x,h)