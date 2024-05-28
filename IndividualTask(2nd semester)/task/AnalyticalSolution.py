import math


class AnalyticalSolution:
    def __init__(self, path_length: float, height: float, body_volume: float, body_weight: float, k: float, speed: float) -> None:
        self.__path_length: float = path_length   # длина пути
        self.__height: float = height             # глубина
        self.__g: float = 9.8                     # ускорение свободного падения
        self.__density_of_water: float = 1000.0   # плотность воды
        self.__body_volume: float = body_volume   # объем подводной лодки
        self.__body_weight: float = body_weight   # масса подводной лодки
        self.__k: float = k                       # константа
        self.__speed: float = speed               # скорость

        self.__time_values: list[float] = list()  # время
        self.__x_values: list[float] = list()     # значения x
        self.__y_values: list[float] = list()     # значения y
        self.__lift_time = None                   # время подъема
        self.__delta_t = 0.1                      # шаг

    def calculate_lift_time(self) -> None:
        self.__lift_time = math.log((1 - self.__path_length * self.__k / (self.__body_weight * self.__speed)) ** (-self.__body_weight / self.__k))

    def calculate_the_archimedes_force(self) -> float:
        archimedes_force = self.__k * self.__height/(math.log((1 - self.__path_length * self.__k/(self.__body_weight*self.__speed)) ** (-self.__body_weight/self.__k)) - self.__path_length/self.__speed) + self.__body_weight * self.__g
        return archimedes_force

    def __generate_time_values(self) -> None:
        time = 0
        while time <= self.__lift_time:
            time += self.__delta_t
            self.__time_values.append(time)

    def __generate_x_values(self) -> None:
        if self.__lift_time is None:
            self.calculate_lift_time()

        time = 0
        while time <= self.__lift_time:
            self.__x_values.append(
                (self.__body_weight*self.__speed/self.__k)*(1-math.exp(-self.__k*time/self.__body_weight))
            )

            time += self.__delta_t

    def __generate_y_values(self) -> None:
        if self.__lift_time is None:
            self.calculate_lift_time()

        time = 0
        while time <= self.__lift_time:
            self.__y_values.append(
                (self.__height / (math.log((1 - self.__path_length * self.__k / (self.__body_weight * self.__speed))
                                           ** (-self.__body_weight / self.__k)) - self.__path_length / self.__speed)) * (
                            time + (self.__body_weight / self.__k) * (math.exp(-(self.__k * time) / self.__body_weight) - 1)) - self.__height
            )

            time += self.__delta_t

    def get_trajectory(self) -> tuple[list[float], list[float]]:
        self.__generate_x_values()
        self.__generate_y_values()
        print(f"Время подъема {self.__lift_time}")

        return self.__x_values, self.__y_values

    def get_depth_versus_time(self) -> tuple[list[float], list[float]]:
        if len(self.__y_values) == 0:
            self.__generate_y_values()

        if len(self.__time_values) == 0:
            self.__generate_time_values()

        return self.__time_values, self.__y_values