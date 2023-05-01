def regressionLine(x, y):
    # We will start creating each one of the operations of the equation.

    x_2 = [i**2 for i in x]
    sum_x_2 = sum(x_2)

    sum_y = sum(y)

    sum_x = sum(x)

    x_y = [x[i]*y[i] for i in range(len(x))]
    sum_x_y = sum(x_y)

    sum_x__2 = sum_x**2

    # We will put each operation in the equation and will solve it to round it later.
    a = round((sum_x_2*sum_y-sum_x*sum_x_y) /
              (len(x)*sum_x_2-sum_x__2), 4)

    b = round((len(x)*sum_x_y-sum_x*sum_y) /
              (len(x)*sum_x_2-sum_x__2), 4)

    result = (a, b)

    return result
