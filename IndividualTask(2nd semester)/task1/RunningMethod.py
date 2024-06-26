
class RunningMethod:

    @staticmethod
    def solution(a, b):
        n = len(a)
        x = [0 for k in range(0, n)]  # обнуление вектора решений

        # Прямой ход
        v = [0 for k in range(0, n)]
        u = [0 for k in range(0, n)]

        # для первой 0-й строки
        v[0] = a[0][1] / (-a[0][0])
        u[0] = (- b[0]) / (-a[0][0])

        for i in range(1, n - 1):  # заполняем за исключением 1-й и (n-1)-й строк матрицы
            v[i] = a[i][i + 1] / (-a[i][i] - a[i][i - 1] * v[i - 1])
            u[i] = (a[i][i - 1] * u[i - 1] - b[i]) / (-a[i][i] - a[i][i - 1] * v[i - 1])

        # для последней (n-1)-й строки
        v[n - 1] = 0
        u[n - 1] = (a[n - 1][n - 2] * u[n - 2] - b[n - 1]) / (-a[n - 1][n - 1] - a[n - 1][n - 2] * v[n - 2])

        # Обратный ход
        x[n - 1] = u[n - 1]
        for i in range(n - 1, 0, -1):
            x[i - 1] = v[i - 1] * x[i] + u[i - 1]

        return x