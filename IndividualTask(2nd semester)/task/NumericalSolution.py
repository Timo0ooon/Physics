import RunningMethod


class NumericalSolution:
    def __init__(self, path_length: float, height: float, n: int, body_volume: float, body_weight: float, k: float,
                 speed: float, time: int) -> None:
        self.__path_length: float = path_length  # длина пути
        self.__height: float = height  # глубина
        self.__n: int = n  # количество шагов
        self.__g: float = 9.8  # ускорение свободного падения
        self.__density_of_water: float = 1000.0  # плотность воды
        self.__body_volume: float = body_volume  # объем подводной лодки
        self.__body_weight: float = body_weight  # масса подводной лодки
        self.__k: float = k  # константа
        self.__speed: float = speed  # скорость
        self.__time: int = time  # время

        self.__h: float = self.__time / n  # длина шага

        self.__time_values: list[float] = [0.0 for _ in range(n)]
        self.__matrix_x: list[list[float]] = [[0.0 for _ in range(n)] for _ in range(n)]  # матрица для x
        self.__matrix_y: list[list[float]] = [[0.0 for _ in range(n)] for _ in range(n)]  # матрица для y

        self.__vector_x: list[float] = [-k * self.__speed for _ in range(n)]  # вектор для матрицы x
        self.__vector_y: list[float] = [  # вектор для матрицы y
            self.__g * (self.__density_of_water * self.__body_volume - self.__body_weight) for _ in range(n)]

        """ НАЧАЛЬНЫЕ УСЛОВИЯ """
        self.__matrix_x[0][0] = 1
        self.__matrix_x[n - 1][n - 1] = 1
        self.__vector_x[0] = 0
        self.__vector_x[self.__n - 1] = self.__path_length

        self.__matrix_y[0][0] = 1
        self.__matrix_y[n - 1][n - 1] = 1
        self.__vector_y[0] = -self.__height
        self.__vector_y[n - 1] = 0

    def __generate_time_values(self) -> None:
        for k in range(self.__n):
            time = k * self.__h

            self.__time_values[k] = time

    def __generate_matrix_x(self) -> None:

        for k in range(1, self.__n - 1):
            self.__matrix_x[k][k - 1] = self.__body_weight / self.__h ** 2
            self.__matrix_x[k][k] = -2 * self.__body_weight / self.__h ** 2
            self.__matrix_x[k][k + 1] = self.__body_weight / self.__h ** 2

    def __generate_matrix_y(self) -> None:

        for k in range(1, self.__n - 1):
            self.__matrix_y[k][k] = -2 * self.__body_weight / self.__h ** 2
            self.__matrix_y[k][k + 1] = self.__body_weight / self.__h ** 2 + self.__k / (2 * self.__h)
            self.__matrix_y[k][k - 1] = self.__body_weight / self.__h ** 2 - self.__k / (2 * self.__h)

    def __solve_matrix_x(self) -> list[float]:
        self.__generate_matrix_x()

        return RunningMethod.RunningMethod.solution(self.__matrix_x, self.__vector_x)

    def __solve_matrix_y(self) -> list[float]:
        self.__generate_matrix_y()

        return RunningMethod.RunningMethod.solution(self.__matrix_y, self.__vector_y)

    def get_trajectory(self) -> tuple[list[float], list[float]]:
        x_values = self.__solve_matrix_x()
        y_values = self.__solve_matrix_y()

        return x_values, y_values

    def get_depth_versus_time(self) -> tuple[list[float], list[float]]:
        self.__generate_time_values()
        y_values = self.__solve_matrix_y()

        return self.__time_values, y_values


if __name__ == "__main__":
    solution = NumericalSolution(500.0, 300.0, 1_000, 20_000.0, 18_700_000, 10.0, 16.5, 30)

