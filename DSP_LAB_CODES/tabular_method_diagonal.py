def diagonal_convolution(x, h):

    m = len(x)
    n = len(h)

    table = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            table[i][j] = x[i] * h[j]

    print("Product Table:\n")

    for row in table:
        print(row)

    y = [0] * (m + n - 1)

    for i in range(m):
        for j in range(n):
            y[i + j] += table[i][j]

    print("\nDiagonal Summation Output:")
    print(y)

x = [4, 2, 1, 3]
h = [1, 2, 2, 1]

diagonal_convolution(x, h)