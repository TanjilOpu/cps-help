def matrix_convolution(x, h):

    m = len(x)
    n = len(h)

    rows = m + n - 1

    H = [[0 for _ in range(m)] for _ in range(rows)]

    for i in range(rows):
        for j in range(m):

            if 0 <= i - j < n:
                H[i][j] = h[i - j]

    Y = []

    for i in range(rows):

        s = 0

        for j in range(m):
            s += H[i][j] * x[j]

        Y.append(s)

    print("Convolution Matrix H:\n")

    for row in H:
        print(row)

    print("\nInput Vector X:\n")

    for value in x:
        print([value])

    print("\nOutput Y = HX:\n")

    for value in Y:
        print([value])

x = [4, 2, 1, 3]
h = [1, 2, 2, 1]

matrix_convolution(x, h)