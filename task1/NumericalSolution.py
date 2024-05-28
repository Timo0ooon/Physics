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

        self.__body_density: float = self.__body_weight / self.__body_volume  # плотность подводной лодки
        self.__h: float = self.__time / n  # длина шага

        self.__t_values: list[float] = [0.0 for _ in range(n)]   # время
        self.__x_values: list[float] = [0.0 for _ in range(n)]   # значения для x
        self.__matrix_y: list[list[float]] = [[0.0 for _ in range(n)] for _ in range(n)]  # матрица для y

        self.__vector_y: list[float] = [  # вектор для матрицы y
            self.__g*(self.__density_of_water - self.__body_density)/self.__body_density for _ in range(n)]

        """ НАЧАЛЬНЫЕ УСЛОВИЯ """
        self.__matrix_y[0][0] = 1
        self.__matrix_y[n - 1][n - 1] = 1
        self.__vector_y[0] = -self.__height
        self.__vector_y[n - 1] = 0

    def __generate_t_values(self) -> None:
        for k in range(self.__n):
            time = k * self.__h

            self.__t_values[k] = time

    def __generate_x_values(self) -> None:
        self.__generate_t_values()

        for k in range(self.__n):
            speed_value = self.__t_values[k] * self.__speed

            self.__x_values[k] = speed_value

    def __generate_matrix_y(self) -> None:

        for k in range(1, self.__n - 1):
            self.__matrix_y[k][k] = -2 / self.__h ** 2
            self.__matrix_y[k][k + 1] = 1 / self.__h**2
            self.__matrix_y[k][k - 1] = 1 / self.__h**2

    def __solve_matrix_y(self) -> list[float]:
        self.__generate_matrix_y()

        return RunningMethod.RunningMethod.solution(self.__matrix_y, self.__vector_y)

    def get_trajectory(self) -> tuple[list[float], list[float]]:
        self.__generate_x_values()
        x_values = self.__x_values
        y_values = self.__solve_matrix_y()

        return x_values, y_values
    
    def get_depth_versus_time(self) -> tuple[list[float], list[float]]:
        self.__generate_t_values()
        y_values = self.__solve_matrix_y()

        return self.__t_values, y_values