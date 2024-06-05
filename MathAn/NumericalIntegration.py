import math


class NumericalIntegration:

    @staticmethod
    def left_rectangle_method(f, x1, x2, n):
        h = abs(x2 - x1)/n
        return sum(f(x1 + h * i) * h for i in range(n))

    @staticmethod
    def right_rectangle_method(f, x1, x2, n):
        h = abs(x2 - x1)/n
        return sum(f(x1 + i * h) * h for i in range(1, n + 1))

    @staticmethod
    def middle_rectangle_method(f, x1, x2, n):
        h = abs(x2 - x1)/n
        return sum(f(x1 + (i + 0.5) * h) * h for i in range(n))

    @staticmethod
    def trapezoid_method(f, x1, x2, n):
        h = abs(x2 - x1)/n
        return sum(h * (f(x1 + i * h) + f(x1 + (i + 1) * h))/2 for i in range(n))

    @staticmethod
    def simpson_method(f, x1, x2, n):
        h = abs(x2 - x1)/n
        return sum(h/6 * (f(x1 + i*h) + 4*f(x1 + (i + 0.5)*h) + f(x1 + (i + 1)*h)) for i in range(n))

    @staticmethod
    def boule_method(f, x1, x2, n):
        h = abs(x2 - x1) / n
        return sum((2 * h)/45 * (7 * f(x1 + i * h) + 32 * f(x1 + (1 + i) * h) + 12 * f(x1 + (2 + i) * h) + 32 * f(x1 + (3 + i) * h) + 7 * f(x1 + (4 + i) * h)) for i in range(0, n, 4))


if __name__ == '__main__':
    function = lambda x: math.e**(-x**2)
    print(round(NumericalIntegration.left_rectangle_method(function, 0, 0.5, 2), 6))
    print(round(NumericalIntegration.middle_rectangle_method(function, 0, 0.5, 2), 6))
    print(round(NumericalIntegration.right_rectangle_method(function, 0, 0.5, 2), 6))
    print(round(NumericalIntegration.trapezoid_method(function,0, 0.5, 2), 6))
    print(round(NumericalIntegration.simpson_method(function, 0, 0.5, 2), 6))
    print(round(NumericalIntegration.boule_method(function, 0, 0.5, 4), 6))
